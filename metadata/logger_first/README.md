# Logger-first L0 -> L0M: findings and choices

**Strategy (2026-09-25).** L0M is the stack of the logger files only (CR1000, historical CR10X, older loggers; plus the
transmissions after the last logger record, see below). No C-level data, no filtering, no convention conversion at L0.
The C-level files (legacy L1 data, Jason's and the per-station ones) fill the gaps at L1 (`liblogger.gapfill_from_c_level`,
called by `GC-Net-level-1-data-processing.py`) until the missing logger data are found; the filled values are tracked
and illustrated (`figures/L1_gapfill`), and only they receive the legacy C-level conversions. Problems are handled at L1
(`metadata/flags`, `metadata/adjustments`, `PROMICE_toolbox.py`). The configuration that drives the CR10X reader lives next to the other L0 settings in `L0/L0_ini/`;
this folder holds the evidence behind it.

## Configuration
Every raw logger file has a `<file>.toml` configuration file next to it (`L0/<station>/<logger> logger files/`): logger type, column names and the
calibration of each column (`[calibration.<var>]`: `scale` or `scale_pos`/`scale_neg`, `add`, and where it came from). The configuration files are the single
place for decoding and calibration (pressure offset, radiation factors, thermistor factors ...); the station `L0/L0_ini/*_header.ini` files only list the
output fields. A file without a configuration file is not read. Do not repeat a calibration as a manual adjustment: `metadata/adjustments` is for corrections of the
measurement itself (sensor swaps, drift, installation heights). The former `CR10X_*.csv` registries were retired once the configuration files were verified against them.
`metadata/c_level_rh_convention.csv` lists the periods where the C-level files hold RH wrt ice (converted to wrt water when they fill a gap), and
`metadata/c_level_corrections.csv` the factors that correct values of the C-level files (never those of the logger files).
A configuration file can carry `[[ignore_rows]]` tables (`start`, `end`, `reason`): the rows of that period are dropped when the file is read, e.g. records dated
before the installation of the station or the tail of a logger that kept recording after its replacement took over.
A configuration file can also carry `[[calibration_period]]` tables (`variable`, `start`, `end`, `multiply`, `reason`): a factor applied after the `[calibration.<var>]` scale
inside a period, for a factor that belongs to a sensor and not to a logger channel (Crawford Point 1 and Swiss Camp: the radiation sensors are swapped from 2012, see `swap_with_OSWR`).
A configuration file can also carry `[[swap_columns]]` tables (`variables = ["HW1", "HW2"]`, `start`, `end`, `reason`): the two columns (and their `_max/_min/_std` columns) are exchanged inside the period, for two sensors that are read on each other's channel
(South Dome from 2006-07-20 22 UTC: HW1 is the upper sonic ranger, the CR1000 configuration files from 2009 carry the table). The C-level files have the same exchange in `metadata/c_level_swaps.csv` (site, var_a, var_b, t0, t1, reason; applied in `liblogger._read_c_files`): South Dome from 2006-07-20 22 UTC, Saddle 2003-05-01 to 2010-04-29. The rows of `metadata/adjustments` and `flags` for the heights are written on the labels AFTER the exchange.
Stations whose L0M is a legacy table without provenance (LAR1-3, KULU) have no configuration file: their calibration (LAR1/LAR2 McGrath constants) and `ice_to_water` rows stay in `metadata/adjustments`.
The Python utilities are in `lib/` (`from lib import liblogger`).

## Evidence tables (this folder)
| file | made by | what it says |
|---|---|---|
| `c_level_treatment_by_year.csv` | L1 script (`liblogger.yearly_diagnostics`) | per variable, logger file and year: radiation ratio C-level/logger, RH (same wrt water / wrt ice / other), HW (sonic-corrected? swapped with the other sensor?), HW columns equal to a TS column |
| `l1_fill_summary.csv` | L1 script | hours per station, variable and source (logger file, transmission, C-level Jason / station file) entering L1 |
| `logger_vs_clevel_agreement.csv` | L1 script | per variable: hours in both / logger only / C-level only, share of equal values |
| `c_level_gap_assessment.csv` | `tools/logger_vs_clevel_review.py assess` | every window where the logger has data and the C-level file has none, with the evidence and verdict (supported / not supported / unclear) behind the NAN flags written to `metadata/flags` (comment contains "logger-first review 2026-09") |
| `timing_check.csv`, `timestamp_iswr_check.csv` | `tools/logger_timing_check.py`, CARRA ssrd scan | share of hours identical to C-level at shifts of -2..+2 h per station-year; ISWR-vs-CARRA check of the offset candidates |
| `hw_offsets_by_year.csv` | `tools/hw_offsets.py [--write]` | per station, HW sensor and year: constant between the C-level HW and the sonic-corrected raw logger distance (the installation height the C-level processing added), and why a year has none; the offsets are written as `add_cr10x` rows to `metadata/adjustments` (applied only to CR10X-sourced hours) |
| `hw_swap_candidates.csv` | `tools/hw_offsets.py` | file-years where the C-level HW1 (HW2) reproduces the logger's OTHER sensor column: swap or gap-fill in the C-level file, or the logger columns named the other way round. Not decided automatically |
| `rh_convention_by_year.csv` | `tools/rh_ice_windows.py [--write]` | per station, RH sensor and year: is the C-level RH wrt ice or wrt water, is it covered by an `ice_to_water` row; missing rows are added (only C-level-sourced hours are converted) |
| `cr10x_decode_verification.csv` | `tools/cr10x_decode.py verify` | every named CR10X column checked against C-level; names that fail are dropped from the registry |
| `../logger_programs/*.csv` | `tools/logger_programs.py` | measurements, output arrays, notes of the 197 logger programs (sensor, multiplier, offset) |

Working files that can be regenerated (not kept): `out/logger_first_review/c_level_gaps.csv` (written by the L1 script, input of `assess`).
Provenance for L1: `L0M/provenance/<station>_source_windows.csv` (which hours are C-level / CR1000 / CR10X).
Origin plots: `figures/L0_sources/<station>_<group>.png`.

## Decoding of the CR10X files (tools/cr10x_decode.py)
- Files are headerless, have no year column (except Swiss Camp 10m), interleave several output arrays (e.g. 61 = met, 62 = TS) and are cumulative downloads. `-6999` = missing.
- Runs are split at non-rollover backward jumps of the day of year (runs < 100 rows dropped); the start year of each run is the year (1990-2015) whose detrended daily temperature best matches the C-level file.
- Columns are matched to C-level variables by exact copy (> 90 % within 0.011) or linear r >= 0.9, one-to-one (Hungarian assignment). RH and HW columns C-level cannot verify are named from the layout template with range checks (RH 20-105, HW 0.2-9.5) and cross-run consensus; a final verification pass drops names that fail (429 of 7,173).
- Time convention: hhmm = 2400 is next day 00:00; stamps like 13:59 are rounded to the hour; sub-hourly data are averaged over the hour ending at the label (maxima with max).
- The unnamed column 26 of the 28-value layouts is the hourly maximum of VW2 (never below VW2, r ~ 0.99): stored as `VW2_max` (`VW1_max` where it tracks VW1).

## Scaling choices
- Raw values are converted in `CR10X_calibration*.csv`, always with the source of the factor stated. Pressure: the programs write P - 400 (CS105 constants everywhere; CS106 only at Larsen C).
- ISWR: the C-level factor equals the documented 200 almost everywhere. OSWR: C-level uses 186.8 where the header says 200; with 200 the median albedo is ~0.90, with 186.8 ~0.84, so the C-level factor is reused (plausibility argument, not a reference measurement). Several stations (GITS, JAR2, CP2, NGRIP, NASA-U, South Dome, Swiss Camp) have CR10X-era factors of ~60-83 that differ from the CR1000-era header, so the CR1000 header must not be applied to their CR10X files.
- Where a file already holds W/m2 (Summit 2004 "1minute calibrated") the factor is ~1. Where the C-level factor cannot be established the station-level factor is kept.
- Deviation from "raw in L0M": radiation and NR (sign-dependent factors) are calibrated at L0 because mixing raw mV and W/m2 in one column is unsafe.

## What the C-level files did (why the L1 rules exist)
- RH: with respect to ice (clipped at 100) in some periods and to water in others (Saddle: ice 2000-02 and 2005-09, water 2003-04). CR10X-sourced RH is the raw measurement wrt water; the legacy `ice_to_water` rows now skip CR10X-sourced hours.
- HW: C-level = logger HW x sqrt((T+273.15)/273.15) + constant (spread 0.003 m at Saddle): raw logger HW is uncorrected. L1 applies the sonic correction to CR10X-sourced hours (`PROMICE_toolbox.sonic_correct_cr10x_hw`); the legacy `air_temp_sonic_correction` rows skip those hours.
- Timing: 190 of 200 station-years agree with C-level at 0 h. Candidates: NASA-U 2007 (+1 h), Humboldt 2002-03 and JAR1 1997 (-1 h), NASA-E 2006-08 and NEEM 2007 (-2 h; CARRA ssrd puts the logger stamps 2 h off for NASA-E 2006-07 and NEEM 2007 while C-level is at 0). No `time_shift` added yet.
- C-level gaps: 6,827 windows where the logger has data and C-level none; 1,882 (1.06 M h) judged faulty and flagged NAN (frozen values dominate; the HW flags are the weakest evidence). The others are kept.

## Transmissions
Nothing is downloaded any more (the envidat API is gone; `libgcnet.get_transmission` was removed and `getunzip` is disabled).
`liblogger.read_transmissions` reads the local files as L0 data: the copy in `L0/<station>/transmissions/` or the backup made on
2023-01-11 (`L0/backup_transmissions_20230111`), whichever adds more records after the last logger record; only those records
are used. Stations without transmissions (Aurora, CP2, JAR3, KAR, KULU, NGRIP, Petermann Glacier, SMS, LAR) never had any: their
backup files are envidat "Page not found" answers (also the JAR2 copy). Aliases: EastGRIP = `E-GRIP.csv`. The backup is the
compiled record of the former pipeline (1995-2022); its early part equals the C-level data (RH wrt ice included), so it is not used
before the last logger record. The RH/HW convention of transmission-sourced hours still has to be checked.

## Other choices
- The `_max`, `_min`, `_stdev` columns of the C-level files are not read (`libgcnet.read_c_file`): their labels are wrong (a `VW1_max` ranging from -81 to 34 is a temperature). Statistics columns in L0M come from the loggers only.
- A logger file whose C-level comparison is poor (r < 0.9, e.g. Petermann Glacier 2002 where the C-level radiation is uncalibrated) keeps the station-level factor; the C-level factor is not copied.
- L1 (`PROMICE_toolbox`): `SOURCE_CR10X` / `SOURCE_CLEVEL` masks come from `L0M/provenance`. HW1/HW2/HS1/HS2 of CR10X-sourced hours are dropped and refilled from the C-level files, so the existing HW adjustments (sonic correction, swaps, offsets) keep their meaning. C-level RH wrt ice is converted to wrt water when it fills a gap (`convert_c_level_rh_to_water`); no `ice_to_water` adjustment rows remain. Without the configuration file files the old behaviour is kept.

## Report
See `release_note_2026.md` at the root of the repository.

## Open
HW swap candidates (`hw_swap_candidates.csv`) and the HS_combined shifts they cause; HW columns holding TS data (`c_level_treatment_by_year.csv`); Jason C-file is ignored at stations without a CR1000 folder; Swiss Camp 10m has no C-file; time_shift sign convention to confirm before adding offsets.
