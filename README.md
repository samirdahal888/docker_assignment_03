# 📝 3-Tier Todo App

## What is 3-Tier? (Like a Restaurant 🍕)
```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   FRONTEND   │───▶│   BACKEND    │───▶│   DATABASE   │
│  (Web Page)  │    │ (API Server) │    │  (Storage)   │
│   Nginx      │    │   FastAPI    │    │  PostgreSQL  │
└──────────────┘    └──────────────┘    └──────────────┘
     │                                         │
  Exposed                                   Hidden
  Port 8080                              (Not exposed)
```

## Run
```bash
docker-compose up --build
```

## Open Browser
http://localhost:8080

## Stop
```bash
docker-compose down
```

## ✅ Assignment Checklist
- ✅ 3 containers (frontend, backend, database)
- ✅ Docker networking (app-network)
- ✅ Database NOT exposed
- ✅ Docker Compose
- ✅ Volume for data (todo-data)
