# Open Service Broker

A spec-compliant Open Service Broker API built with FastAPI and Docker.

> 🚧 Work in progress 

## Tech Stack
- **FastAPI** — broker API
- **Docker** — provisioning backing services
- **Kubernetes** — platform integration (coming soon)

## Project Structure
- `app/api/v2/` — OSB endpoints (catalog, instances, bindings)
- `app/models/` — Pydantic models
- `app/services/` — Docker SDK calls
- `app/db/` — instance and binding persistence

## Run Locally
```bash
python -m venv .venv
.venv\Scripts\activate
pip install "fastapi[standard]"
uvicorn app.main:app --reload
```

## Endpoints
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/v2/catalog` | List available services and plans |
| PUT | `/v2/service_instances/:id` | Provision a service (coming soon) |
| PUT | `/v2/service_instances/:id/service_bindings/:id` | Bind a service (coming soon) |

## Blog
Full writeup coming on Medium after completion.