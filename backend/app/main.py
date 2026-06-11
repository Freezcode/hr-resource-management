from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.db import Base, engine
from app.routes import agents, auth, employees, reports, surveys, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HR Resource Management", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(tasks.router)
app.include_router(surveys.router)
app.include_router(agents.router)
app.include_router(reports.router)


@app.get("/")
def healthcheck():
    return {"status": "ok", "service": "hr-resource-management"}
