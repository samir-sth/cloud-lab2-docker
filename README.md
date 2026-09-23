# Cloud Computing Lab 2

Simple dynamic Django task manager deployed with Docker Compose.

## Architecture

Browser -> Nginx -> Django/Gunicorn -> PostgreSQL

## Requirements

Only:
- Docker Desktop on Windows, or
- Docker Engine + Docker Compose plugin on Linux
- Git

No local Python, Django, PostgreSQL, Nginx, or virtual environment is required.

## Run

```bash
git clone YOUR_REPOSITORY_URL
cd cloud-lab2-django-docker
docker compose up --build -d
```

Open:

http://localhost:8080

## Check containers

```bash
docker compose ps
```

## View logs

```bash
docker compose logs -f
```

## Stop

```bash
docker compose down
```

## Stop and delete database data too

```bash
docker compose down -v
```

## Rebuild after changing code

```bash
docker compose up --build -d
```
