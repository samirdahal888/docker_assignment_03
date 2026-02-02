# 3-Tier Todo App

A simple todo application using Docker with 3 tiers: Frontend, Backend, and Database.

## Technologies Used

- Frontend: Nginx with HTML/CSS/JavaScript
- Backend: Python FastAPI
- Database: PostgreSQL

## How to Run

```bash
docker-compose up --build
```

Then open http://localhost:8080 in your browser.

## How to Stop

```bash
docker-compose down
```

## Project Structure

- `frontend/` - Nginx web server with HTML page
- `backend/` - FastAPI server with REST API
- `docker-compose.yml` - Connects all services together

## Features

- Add todos
- Delete todos
- Data persists after restart (using Docker volume)

## Docker Setup

- 3 separate containers for each tier
- Private network for container communication
- Database is not exposed to host (only frontend is exposed on port 8080)
- Volume used for persistent data storage
