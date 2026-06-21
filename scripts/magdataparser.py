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
    # header
    if line[0] == "/" and line[1] == "E":
        header = line.lstrip("/").split()
    
    #line id
    if line[0] == "/" and line[1] == "l":
        full_line = line.lstrip("/").split()
        current_line_id = full_line[1]
   
   #data line
    if line[0] != "/":
        #data line
        data_line = line.split()
        row_dict = dict(zip(header, data_line))
        row_dict["line_id"] = current_line_id
        data_rows.append(row_dict)


# 2 Parse file into PD dataframe?
# df = pd.DataFrame(data_rows)

# 3 Create Postgres DB and insert data into?

