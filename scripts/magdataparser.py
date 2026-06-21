### Mag Data Parser Script
### Author: Spencer Morphy
### Date June 21, 2026
### Parses raw mag data into a PostgreSQL db

# import pandas as pd, sqlalchemy

header = None
current_line_id = None
data_rows = []
metadata_lines = []

fd = open("../rawdata/magdataraw.txt", "r")
for line in fd:
    if line[0] == "/" and line[1] == "E":
        print("Header found")
        header = line.lstrip("/").split()
        print(header)

    if line[0] == "/" and line[1] == "l":
        print("Line number updated")
        full_line = line.lstrip("/").split()
        current_line_id = full_line[1]
        print(current_line_id)

    if line[0] != "/":
        #data line
        print("dataline")
        print(line)


# 2 Parse file into PD dataframe?

# 3 Create Postgres DB and insert data into?

