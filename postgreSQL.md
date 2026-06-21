# PostgreSQL Info

Deciding to set up using Docker to run a containerized PostGRES server

```
docker --version
docker ps //lists running containers
docker pull postgres
docker run --name pg-datapipeline -e POSTGRES_PASSWORD=yourpassword -e POSTGRES_DB=magdata -p 5432:5432 -v pgdata:/var/lib/postgresql/data -d postgres:16
docker ps

docker exec -it pg-datapipeline psql -U postgres -d magdata
```

### Python Connection
```
engine = create_engine("postgresql+psycopg2://postgres:yourpassword@localhost:5432/magdata")
```

```
docker stop pg-datapipeline
docker start pg-datapipeline

docker rm -f pg-datapipeline

docker-compose.yaml
```
