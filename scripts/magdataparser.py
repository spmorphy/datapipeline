### Mag Data Parser Script
### Author: Spencer Morphy
### Date June 21, 2026
### Parses raw mag data into a PostgreSQL db

# 1 Open the file
fd = open("../rawdata/magdataraw.txt", "r")
for line in fd:
    if line[0] == "/" and line[1] == "E":
        print("Header found")
        print(line)
        # strip leading / and insert into pandas dataframe as header

    if line[0] != "/":
        #data line
        print("dataline")
        print(line)


# 2 Parse file into PD dataframe?

# 3 Create Postgres DB and insert data into?

