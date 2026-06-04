# datapipeline
Built this repo as a learning project to understand/implement converting raw data sources into SQL databases.

### Places to start:
1. Collect raw data types into dir /raw/
2. Build workflows inserting into POSTgres DB's
3. DB visualization tools? (GUI's)
4. Grafana for DB's interaction
5. EXTRA: (host DB in Docker container, w/ persistent storage: eventually self hosted with Kubernetes deployment.

### Data Sources

1. Geological Data: can pull from public GOV sites (USGS etc.)
2. Free Public API's (https://www.freepublicapis.com/)
3. NASA data (https://data.nasa.gov/organization/nasa)
4. Live Buoy data (Surf report) 


### Workflow

1. From a raw data file
    1. Create a new postgreSQL db 
    2. Check if duplicates and insert new values into postgreSQL db
    3. Delete postgreSQL db

