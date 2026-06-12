# Open Service Broker

A spec-compliant Open Service Broker API built with FastAPI, Docker, and PostgreSQL.

> Work in progress

## Tech Stack
- **FastAPI** — broker API
- **Docker** — provisioning backing services
- **PostgreSQL** — persisting instance and binding state
- **Kubernetes** — platform integration (coming soon)

## Project Structure
- `app/api/v2/` — OSB endpoints (catalog, instances, bindings)
- `app/models/` — Pydantic models
- `app/services/` — Docker SDK calls
- `app/db/` — instance and binding persistence

## Run Locally

Start the database first:
```bash
docker-compose up -d
```

Then run the broker:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints
| Method | Route | Description | Status |
|--------|-------|-------------|--------|
| GET | `/v2/catalog` | List available services and plans | Done |
| PUT | `/v2/service_instances/:id` | Provision a service instance | Done |
| PUT | `/v2/service_instances/:id/service_bindings/:id` | Bind a service | Done |
| DELETE | `/v2/service_instances/:id/service_bindings/:id` | Unbind a service | Done |
| DELETE | `/v2/service_instances/:id` | Deprovision a service | Done |

## Blog
Full writeup on Medium: coming soon

## What's Next
- Containerize the broker with Docker
- Deploy and integrate with Kubernetes