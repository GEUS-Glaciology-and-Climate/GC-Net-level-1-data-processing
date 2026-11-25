# -*- coding: utf-8 -*-
"""Uploads the L1 dataset (L1/hourly, L1/daily, location file, variable list, ReadMe) to the GEUS Dataverse dataset
https://doi.org/10.22008/FK2/VVXGUT as a new DRAFT version. Nothing is published unless you ask for it.

Token: write your Dataverse API token (Dataverse > your name > API Token) in the file  dataverse_token.txt  at the root of the repository
(listed in .gitignore) or in the environment variable DATAVERSE_API_TOKEN. The token is never printed.

Usage (repository root):
  python tools/upload_to_dataverse.py                  plan: pre-flight checks of the files + comparison with what is in the dataset (no changes)
  python tools/upload_to_dataverse.py --check          pre-flight checks only (no network)
  python tools/upload_to_dataverse.py --upload         adds / replaces the files that differ in the draft version of the dataset
  python tools/upload_to_dataverse.py --upload --delete-stale   also removes from the draft the files that are no longer in L1/
  python tools/upload_to_dataverse.py --publish minor  publishes the draft (asks you to type 'publish'; 'major' for a new major version)
Options: --quick (skip the line-by-line timestamp check), --force (upload although the pre-flight checks found errors),
         --with-release-note (also uploads release_note_2026.md in the folder documentation/), --server URL (default https://dataverse.geus.dk).

What is uploaded (the layout of the published version 11): hourly/<station>.csv, daily/<station>_daily.csv, GC-Net_location.csv,
L1_variable_list.csv, _ReadMe_L1.txt. A file whose md5 equals the one in the dataset is skipped (Dataverse refuses duplicates); a file that
exists with another content is replaced (same name, new version of the file); a new file is added. The upload is verified at the end by
comparing the md5 of every local file with the one the server reports.

Pre-flight checks (errors stop the upload): every hourly file has its daily file and the reverse, and the stations are those of
GC-Net_location.csv; each file is a NEAD file with doi 10.22008/FK2/VVXGUT, a '# fields' line whose length equals the number of columns of the data,
timestamps without gaps in the format, strictly increasing and without NaT; the ReadMe no longer says that the files have to be regenerated; the
L1 files are newer than the metadata, the code and the L0 configuration files they were built from (warning otherwise); fields without description in
L1_variable_list.csv (warning).
"""
import os
import sys
import json
import time
import glob
import hashlib
import argparse
import urllib.parse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOI = "doi:10.22008/FK2/VVXGUT"
DOI_SHORT = "10.22008/FK2/VVXGUT"
DEFAULT_SERVER = "https://dataverse.geus.dk"
TOKEN_FILE = os.path.join(ROOT, "dataverse_token.txt")
ROOT_FILES = ["GC-Net_location.csv", "L1_variable_list.csv", "_ReadMe_L1.txt"]


# ----------------------------------------------------------------------------------------------------------------- files
def local_files(with_release_note=False):
    """list of (path, directoryLabel or '', label, description)"""
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "L1", "hourly", "*.csv"))):
        st = os.path.basename(p)[:-4]
        out.append((p, "hourly", os.path.basename(p), "Hourly L1 data of station %s (NEAD format)" % st))
    for p in sorted(glob.glob(os.path.join(ROOT, "L1", "daily", "*.csv"))):
        st = os.path.basename(p)[:-4].replace("_daily", "")
        out.append((p, "daily", os.path.basename(p), "Daily L1 data of station %s (NEAD format)" % st))
    desc = {"GC-Net_location.csv": "Positions of the stations", "L1_variable_list.csv": "Variables of the L1 files, units and descriptions",
            "_ReadMe_L1.txt": "Description of the L1 dataset and of its processing"}
    for n in ROOT_FILES:
        out.append((os.path.join(ROOT, "L1", n), "", n, desc[n]))
    if with_release_note:
        out.append((os.path.join(ROOT, "release_note_2026.md"), "documentation", "release_note_2026.md",
                    "Release note of the 2026 version of the processing"))
    return out


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def norm(s):
    return str(s).lower().replace(" ", "").replace("-", "").replace("_", "")


# ------------------------------------------------------------------------------------------------------------ pre-flight
def read_header(path):
    """returns (metadata dict, fields list, number of header lines)"""
    meta, fields, n = {}, None, 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            n += 1
            if line.startswith("# [DATA]"):
                break
            if line.startswith("# fields"):
                fields = line.split("=", 1)[1].strip().split(",")
            elif line.startswith("# ") and "=" in line:
                k, v = line[2:].split("=", 1)
                meta[k.strip()] = v.strip()
    return meta, fields, n


def preflight(files, quick=False):
    import pandas as pd
    errors, warnings = [], []
    hourly = {os.path.basename(p)[:-4]: p for p, d, _, _ in files if d == "hourly"}
    daily = {os.path.basename(p)[:-10]: p for p, d, _, _ in files if d == "daily"}
    for s in sorted(set(hourly) - set(daily)):
        errors.append("no daily file for " + s)
    for s in sorted(set(daily) - set(hourly)):
        errors.append("no hourly file for " + s)
    for n in ROOT_FILES:
        if not os.path.isfile(os.path.join(ROOT, "L1", n)):
            errors.append("missing L1/" + n)
    # stations of the location file
    try:
        loc = pd.read_csv(os.path.join(ROOT, "L1", "GC-Net_location.csv"), skipinitialspace=True, encoding="utf-8-sig")
        names = {norm(x) for x in loc["Name"]}
        for s in hourly:
            if norm(s) not in names:
                warnings.append("%s is not in GC-Net_location.csv" % s)
    except Exception as e:
        warnings.append("cannot read GC-Net_location.csv: %s" % e)
    # variable list
    described = set()
    try:
        described = set(pd.read_csv(os.path.join(ROOT, "L1", "L1_variable_list.csv"), encoding="utf-8-sig")["fields"].astype(str).str.strip())
    except Exception as e:
        warnings.append("cannot read L1_variable_list.csv: %s" % e)
    undescribed = set()
    # ReadMe
    try:
        rd = open(os.path.join(ROOT, "L1", "_ReadMe_L1.txt"), encoding="utf-8", errors="replace").read()
        if "have to be regenerated" in rd or "files of this folder are the ones of the previous version" in rd:
            errors.append("_ReadMe_L1.txt still says that the files have to be regenerated (section 'Status of this folder')")
    except Exception:
        pass
    # staleness
    l1_oldest = min(os.path.getmtime(p) for p, d, _, _ in files if d in ("hourly", "daily"))
    sources = glob.glob(os.path.join(ROOT, "metadata", "adjustments", "*.csv")) + glob.glob(os.path.join(ROOT, "metadata", "flags", "*.csv")) + \
        glob.glob(os.path.join(ROOT, "L0", "**", "*.toml"), recursive=True) + [os.path.join(ROOT, "lib", "PROMICE_toolbox.py"),
                                                                              os.path.join(ROOT, "GC-Net-level-1-data-processing.py")]
    newer = [s for s in sources if os.path.isfile(s) and os.path.getmtime(s) > l1_oldest]
    for s in newer[:10]:
        warnings.append("built before its source was edited: %s" % os.path.relpath(s, ROOT))
    if len(newer) > 10:
        warnings.append("... and %d more sources newer than the oldest L1 file" % (len(newer) - 10))
    # each data file
    for p, d, label, _ in files:
        if d not in ("hourly", "daily"):
            continue
        if os.path.getsize(p) < 1000:
            errors.append(label + ": smaller than 1 kB")
            continue
        meta, fields, nh = read_header(p)
        if fields is None:
            errors.append(label + ": no '# fields' line")
            continue
        if not meta.get("doi", "").endswith(DOI_SHORT):
            errors.append(label + ": doi in the header is '%s'" % meta.get("doi", ""))
        for x in fields:       # <var>_qc and <var>_adj_flag are derived from the described variables (lib/PROMICE_toolbox.py, field_info)
            base = x[:-len("_adj_flag")] if x.endswith("_adj_flag") else (x[:-3] if x.endswith("_qc") else x)
            if described and base not in described:
                undescribed.add(x)
        with open(p, encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i >= nh and line.strip() and not line.startswith("#"):      # first data line (empty comment lines follow [DATA])
                    ncol = len(line.rstrip("\r\n").split(","))
                    if ncol != len(fields):
                        errors.append("%s: %d fields in the header, %d columns in the data" % (label, len(fields), ncol))
                    break
        if quick:
            continue
        t = pd.read_csv(p, comment="#", header=None, usecols=[0], names=["t"], dtype=str)["t"]
        ts = pd.to_datetime(t, utc=True, errors="coerce")
        if ts.isna().any():
            errors.append("%s: %d timestamps cannot be read (first at line %d)" % (label, int(ts.isna().sum()), int(ts.isna().idxmax()) + nh + 1))
        elif not ts.is_monotonic_increasing or ts.duplicated().any():
            errors.append("%s: timestamps not strictly increasing" % label)
    if undescribed:
        warnings.append("fields of the files without description in L1_variable_list.csv: " + ", ".join(sorted(undescribed)))
    return errors, warnings


# -------------------------------------------------------------------------------------------------------------- server
class Dataverse:
    def __init__(self, server, token):
        import requests
        self.s = requests.Session()
        self.server = server.rstrip("/")
        self.token = token

    def _h(self):
        return {"X-Dataverse-key": self.token} if self.token else {}

    def get(self, path, **kw):
        r = self.s.get(self.server + path, headers=self._h(), timeout=120, **kw)
        r.raise_for_status()
        return r.json()

    def version_files(self, version):
        q = "?persistentId=" + urllib.parse.quote(DOI)
        j = self.get("/api/datasets/:persistentId/versions/%s%s" % (version, q))["data"]
        return j, {(f.get("directoryLabel", "") or "") + "/" + f["label"]: f for f in j["files"]}

    def state(self):
        """(version dict, files dict) of the draft if there is one, otherwise of the latest published version"""
        if self.token:
            try:
                return self.version_files(":draft")
            except Exception:
                pass
        return self.version_files(":latest-published")

    def post_file(self, url, path, label, jsonData, tries=3):
        import requests
        from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
        size = os.path.getsize(path)
        for k in range(tries):
            try:
                with open(path, "rb") as fh:
                    enc = MultipartEncoder(fields={"file": (label, fh, "text/csv" if label.endswith(".csv") else "text/plain"),
                                                   "jsonData": json.dumps(jsonData)})
                    done = [0]

                    def cb(m):
                        pct = int(100 * m.bytes_read / max(m.len, 1))
                        if pct != done[0] and pct % 20 == 0:
                            done[0] = pct
                            print("      %3d %%" % pct, end="\r", flush=True)
                    mon = MultipartEncoderMonitor(enc, cb)
                    r = self.s.post(url, data=mon, headers=dict(self._h(), **{"Content-Type": mon.content_type}), timeout=(30, 1800))
                if r.status_code in (200, 201):
                    return r.json()
                if r.status_code < 500:
                    raise RuntimeError("%s: HTTP %d %s" % (label, r.status_code, r.text[:300]))
                err = "HTTP %d %s" % (r.status_code, r.text[:200])
            except (requests.ConnectionError, requests.Timeout) as e:
                err = str(e)[:200]
            print("      attempt %d of %d failed (%s)" % (k + 1, tries, err))
            time.sleep(10 * (k + 1))
        raise RuntimeError("%s: upload failed after %d attempts" % (label, tries))

    def add(self, path, directory, label, description):
        jd = {"description": description, "restrict": False, "categories": ["Data"] if directory else ["Documentation"]}
        if directory:
            jd["directoryLabel"] = directory
        return self.post_file(self.server + "/api/datasets/:persistentId/add?persistentId=" + urllib.parse.quote(DOI), path, label, jd)

    def replace(self, file_id, path, directory, label, description):
        jd = {"description": description, "forceReplace": True, "restrict": False}
        if directory:
            jd["directoryLabel"] = directory
        return self.post_file("%s/api/files/%d/replace" % (self.server, file_id), path, label, jd)

    def delete(self, file_id):
        import requests
        r = self.s.delete("%s/dvn/api/data-deposit/v1.1/swordv2/edit-media/file/%d" % (self.server, file_id), auth=(self.token, ""), timeout=120)
        if r.status_code not in (200, 204):
            raise RuntimeError("delete %d: HTTP %d %s" % (file_id, r.status_code, r.text[:200]))

    def publish(self, kind):
        import requests
        r = self.s.post("%s/api/datasets/:persistentId/actions/:publish?persistentId=%s&type=%s" % (self.server, urllib.parse.quote(DOI), kind),
                        headers=self._h(), timeout=300)
        if r.status_code != 200:
            raise RuntimeError("publish: HTTP %d %s" % (r.status_code, r.text[:300]))
        return r.json()


def read_token():
    if os.path.isfile(TOKEN_FILE):
        t = open(TOKEN_FILE, encoding="utf-8").read().strip()
        if t:
            return t
    return os.environ.get("DATAVERSE_API_TOKEN", "").strip()


def plan(files, remote):
    """classifies the local files against the remote ones: unchanged / replace / add, and the remote files without local counterpart"""
    out = []
    for p, d, label, desc in files:
        key = (d + "/" if d else "/") + label
        r = remote.get(key)
        if r is None:
            out.append(("add", p, d, label, desc, None))
        elif md5(p) == r["dataFile"].get("md5"):
            out.append(("same", p, d, label, desc, r))
        else:
            out.append(("replace", p, d, label, desc, r))
    local_keys = {(d + "/" if d else "/") + label for _, d, label, _ in files}
    stale = [r for k, r in remote.items() if k not in local_keys]
    return out, stale


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--upload", action="store_true")
    ap.add_argument("--delete-stale", action="store_true")
    ap.add_argument("--publish", choices=["minor", "major"])
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--with-release-note", action="store_true")
    ap.add_argument("--server", default=DEFAULT_SERVER)
    a = ap.parse_args()

    files = local_files(a.with_release_note)
    print("%d local files (%.0f MB) from L1/" % (len(files), sum(os.path.getsize(p) for p, _, _, _ in files) / 1e6))
    errors, warnings = preflight(files, a.quick)
    for w in warnings:
        print("WARNING:", w)
    for e in errors:
        print("ERROR:", e)
    print("pre-flight: %d errors, %d warnings" % (len(errors), len(warnings)))
    if a.check:
        sys.exit(1 if errors else 0)

    token = read_token()
    if (a.upload or a.publish) and not token:
        sys.exit("no token: put it in dataverse_token.txt (repository root) or DATAVERSE_API_TOKEN")
    if a.upload and errors and not a.force:
        sys.exit("errors in the pre-flight checks: fix them or use --force")
    dv = Dataverse(a.server, token)

    if a.publish and not a.upload:
        ver, _ = dv.version_files(":draft")
        print("draft version of the dataset: %s, %d files" % (ver.get("versionState"), len(ver["files"])))
        if input("type 'publish' to publish this draft as a %s version: " % a.publish).strip() != "publish":
            sys.exit("not published")
        print(json.dumps(dv.publish(a.publish)["data"].get("versionState")))
        return

    ver, remote = dv.state()
    print("dataset %s: %s version %s.%s with %d files (%s)" % (DOI, ver.get("versionState"), ver.get("versionNumber"), ver.get("versionMinorNumber"),
                                                              len(remote), "draft" if ver.get("versionState") == "DRAFT" else "no draft yet"))
    todo, stale = plan(files, remote)
    for kind in ("add", "replace", "same"):
        n = [x for x in todo if x[0] == kind]
        print("  %-8s %3d files%s" % (kind, len(n), (": " + ", ".join(x[3] for x in n[:6]) + (" ..." if len(n) > 6 else "")) if kind != "same" and n else ""))
    print("  stale    %3d files in the dataset that are not in L1/%s" % (len(stale), (": " + ", ".join(r["label"] for r in stale[:8])) if stale else ""))
    if not a.upload:
        print("plan only; use --upload to apply it (draft version, nothing is published)")
        return

    for kind, p, d, label, desc, r in todo:
        if kind == "same":
            continue
        print("%s %s/%s (%.1f MB)" % (kind, d, label, os.path.getsize(p) / 1e6), flush=True)
        if kind == "add":
            dv.add(p, d, label, desc)
        else:
            dv.replace(r["dataFile"]["id"], p, d, label, desc)
    if a.delete_stale:
        for r in stale:
            print("delete", r.get("directoryLabel", ""), r["label"])
            dv.delete(r["dataFile"]["id"])

    # verification
    ver, remote = dv.version_files(":draft")
    bad = []
    for p, d, label, _ in files:
        r = remote.get((d + "/" if d else "/") + label)
        if r is None or r["dataFile"].get("md5") != md5(p):
            bad.append(label)
    print("verification: %d of %d local files identical to the draft on the server%s" % (len(files) - len(bad), len(files), (" (differ: " + ", ".join(bad) + ")") if bad else ""))
    print("draft: %s/dataset.xhtml?persistentId=%s&version=DRAFT  (review it, then publish from the web page or with --publish minor)" % (a.server, DOI))
    if a.publish:
        if bad:
            sys.exit("not publishing: the draft differs from the local files")
        if input("type 'publish' to publish this draft as a %s version: " % a.publish).strip() != "publish":
            sys.exit("not published")
        print(dv.publish(a.publish)["data"].get("versionState"))


if __name__ == "__main__":
    main()
