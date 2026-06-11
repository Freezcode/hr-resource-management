# HR Resource Management (CrewAI + FastAPI + React)

AI-powered HR resource management platform to analyze productivity and workplace climate with specialized CrewAI agents.

## Features

- Productivity analysis (completion rates, bottlenecks, blocked work)
- Work climate analysis (engagement, stress, sentiment)
- Resource planning (workload balancing, capacity insights)
- Multi-agent orchestration with CrewAI
- Dashboard-ready combined reports and action plans
- Role-ready JWT authentication flow

## Project Structure

```text
hr-resource-management/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── agents/
│   │   ├── tools/
│   │   ├── models/
│   │   ├── database/
│   │   └── routes/
│   ├── requirements.txt
│   ├── .env.example
│   └── run.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── App.jsx
│   ├── package.json
│   └── vite.config.js
├── database/
│   └── schema.sql
└── docker-compose.yml
```

## CrewAI Agents

1. **Productivity Analyst Agent** – task throughput and bottleneck detection
2. **Climate Researcher Agent** – survey and climate interpretation
3. **Resource Planner Agent** – workload and capacity optimization
4. **Report Generator Agent** – executive summary generation
5. **Action Coordinator Agent** – cross-agent orchestration and action planning

## Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python run.py
```

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## API Overview

- `POST /auth/register`
- `POST /auth/token`
- `GET/POST /employees`
- `GET/POST /tasks`
- `GET/POST /surveys`
- `GET /agents/catalog`
- `POST /agents/run`
- `GET /reports/dashboard`

Protected endpoints require a JWT access token in the Authorization header.

## Docker

```bash
docker compose up --build
```

This starts:
- PostgreSQL on `5432`
- FastAPI backend on `8000`
- React frontend on `5173`
