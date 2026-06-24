# datapipeline
Built this repo as a learning project to understand/implement converting raw data sources into SQL databases.

### Overview Work Schedule:
1. Collect raw data types into dir /rawdata/
2. Build workflows/scripts inserting into POSTgres DB's
3. DB visualization tools? (GUI's)
4. Grafana for DB's interaction
5. EXTRA: (host DB in Docker container, w/ persistent storage: eventually self hosted with Kubernetes deployment.

### Data Sources
1. Geological Data: can pull from public GOV sites (USGS etc.)
2. Free Public API's (https://www.freepublicapis.com/)
3. NASA data (https://data.nasa.gov/organization/nasa)
4. Live Buoy data (Surf report)


### Workflow
1. Raw data file
2. Python script
    1. Parse data
    2. Convert into PANDAS dataframe
    3. Insert into postgreSQL DB using SQalcehmy
3. Dockerfile:
    1. Create SQL database ->> work here.
