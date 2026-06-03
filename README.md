open-service-broker/
│
├── app/
│   ├── api/
│   │   └── v2/
│   │       ├── catalog.py          # GET /v2/catalog
│   │       ├── instances.py        # Provision / Deprovision
│   │       └── bindings.py         # Bind / Unbind
│   │
│   ├── models/
│   │   ├── catalog.py              # Pydantic models for catalog
│   │   ├── instances.py            # Pydantic models for instances
│   │   └── bindings.py             # Pydantic models for bindings
│   │
│   ├── services/
│   │   └── docker_service.py       # All Docker SDK calls live here
│   │
│   ├── db/
│   │   └── database.py             # Stores instance + binding state
│   │
│   └── main.py                     # FastAPI app entry point
│
├── tests/
│   ├── test_catalog.py
│   ├── test_instances.py
│   └── test_bindings.py
│
├── docker-compose.yml              # Runs broker + its database together
├── Dockerfile                      # Packages your broker
├── requirements.txt
└── README.md