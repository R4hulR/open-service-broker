# Open Service Broker

A spec-compliant Open Service Broker API built with FastAPI and Docker.

> 🚧 Work in progress

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
| GET | `/v2/catalog` | List available services and plans | ✅ |
| PUT | `/v2/service_instances/:id` | Provision a service instance | ✅ |
| PUT | `/v2/service_instances/:id/service_bindings/:id` | Bind a service | 🚧 |
| DELETE | `/v2/service_instances/:id` | Deprovision a service | 🚧 |
| DELETE | `/v2/service_instances/:id/service_bindings/:id` | Unbind a service | 🚧 |

## Blog
Full writeup coming on Medium after completion.