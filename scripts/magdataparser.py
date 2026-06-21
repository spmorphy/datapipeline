### Mag Data Parser Script
### Author: Spencer Morphy
### Date June 21, 2026
### Parses raw mag data into a PostgreSQL db

import pandas as pd 
import sqlalchemy import create_engine
# import psycopg2

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


# 2 Parse file into PD dataframe
df = pd.DataFrame(data_rows)
# ['Easting', 'Northing', 'elevation', 'nT', 'sq', cor-nT', 'sat', 'position-type','time', 'picket-x', picket-y']

df["Easting"] = pd.to_numeric(df["Easting"])
df["Northing"] = pd.to_numeric(df["Northing"])
df["elevation"] = pd.to_numeric(df["elevation"])
df["nT"] = pd.to_numeric(df["nT"])
df["sq"] = pd.to_numeric(df["sq"])
df["cor-nT"] = pd.to_numeric(df["cor-nT"])
# df["position-type"] = pd.to_numeric(df["position-type"])

# df["time"] = pd.to_datetime(df["time"])
df["picket-x"] = pd.to_numeric(df["picket-x"], errors="coerce")
df["picket-y"] = pd.to_numeric(df["picket-y"], errors="coerce")

print(df.head(10))

# 3 Create Postgres DB

engine = create_engine("postgresql+psycopg2://username:password@localhost:5432/magdata")
df.to_sql("survey_data", engine, if_exists="replace", index=False)
