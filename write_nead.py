from io import StringIO
import configparser
from pathlib import Path
import nead
import numpy as np


def read_config(config_path: str):
    config_file = Path(config_path)

    # Load configuration file
    config = configparser.RawConfigParser(
        inline_comment_prefixes="#", allow_no_value=True
    )
    config.read(config_file)

    if len(config.sections()) < 1:
        print("Invalid config file, missing sections")
        return None

    return config


# Assign hash_lines with config lines prepended with '# '
def get_hashed_lines(config):
    hash_lines = []
    for line in config.replace("\r\n", "\n").split("\n"):
        line = "# " + line + "\n"
        hash_lines.append(line)
    return hash_lines


# Writes NEAD file (CSV file with NEAD formatted header)
# Columns written in NEAD output will be the fields designated in the
#   NEAD configuration file setting 'fields' in section 'FIELDS'
# Paths must be absolute
# Paths can use 'r' in front of strings with paths to designate them as a raw string if using Windows
#   style paths with backslashes
# Arguments:
#   data_frame    Pandas dataframe
#   nead_config   string with Path to NEAD configuration file, ex. r'C:\Users\Icy\gcnet\config\nead_header.ini'
#   output_path   string with Path assigned to output NEAD file,
#                 be sure to designate name for new NEAD file at end of string
#                 ex.  r'C:\Icy\gcnet\output\nead\my_nead_file_name')
def write_nead(data_frame, nead_config, output_path):

    # Assign nead_output to output_path with .csv extension
    nead_output = Path("{0}.csv".format(output_path))

    # Read nead_config into conf
    conf = read_config(Path(nead_config))

    # Assign fields from nead_config 'fields', convert to list in fields_list
    fields = conf.get("FIELDS", "fields")
    fields_list = fields.split(",")

    # fields_list = [f for f in fields_list if f in data_frame.columns]

    for f in fields_list:
        if f not in data_frame.columns:
            data_frame[f] = np.nan

    # Write conf into buffer
    buffer = StringIO()
    conf.write(buffer)

    # Assign hash_lines with nead_config lines prepended with '# '
    hash_lines = get_hashed_lines(buffer.getvalue())

    # Write hash_lines into nead_header
    with open(nead_output, "w", newline="\n") as nead_header:
        nead_header.write("# NEAD 1.0 UTF-8\n")
        for row in hash_lines:
            nead_header.write(row)

    # Append data to header, omit indices, omit dataframe header, and output columns in fields_list
    with open(nead_output, "a") as nead_file:
        # print(fields_list)
        data_frame.to_csv(
            nead_file,
            index=False,
            header=False,
            columns=fields_list,
            line_terminator="\n",
            float_format="%.2f",
        )

    ds = nead.read(nead_output)


# get list of values from nead config [FIELDS] section
# this is for getting the calibration parameters
def get_config_list(nead_config, config_key):  # Read nead_config into conf
    conf = read_config(
        Path(nead_config)
    )  # Assign values from nead_config 'config_key', convert to list in values_list
    values_string = conf.get("FIELDS", config_key)
    values_list = values_string.split(",")
    values_list_float = [float(item) for item in values_list]
    return values_list_float


def get_config_list_str(nead_config, config_key):  # Read nead_config into conf
    conf = read_config(
        Path(nead_config)
    )  # Assign values from nead_config 'config_key', convert to list in values_list
    values_string = conf.get("FIELDS", config_key)
    values_list = values_string.split(",")
    return values_list
