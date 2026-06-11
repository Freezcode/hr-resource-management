from typing import Any

from app.tools.analysis_tools import plan_resource_actions

try:
    from crewai import Agent
except Exception:
    Agent = None


def build_resource_planner_agent() -> Any:
    if Agent is None:
        return {
            "role": "Resource Planner",
            "goal": "Optimize workload and team capacity",
        }

    return Agent(
        role="Resource Planner",
        goal="Optimize capacity, identify skill gaps, and balance team workload",
        backstory="You ensure the right people are assigned to the right priorities.",
        verbose=True,
    )


def analyze_resources(resource_data: dict) -> dict:
    return {
        "actions": plan_resource_actions(resource_data),
        "avg_tasks_per_employee": resource_data.get("avg_tasks_per_employee", 0),
    }
