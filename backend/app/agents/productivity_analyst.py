from typing import Any

from app.tools.analysis_tools import identify_productivity_bottlenecks

try:
    from crewai import Agent
except Exception:
    Agent = None


def build_productivity_analyst_agent() -> Any:
    if Agent is None:
        return {
            "role": "Productivity Analyst",
            "goal": "Analyze task throughput and identify bottlenecks",
        }

    return Agent(
        role="Productivity Analyst",
        goal="Analyze task completion rates, time tracking, and project progress",
        backstory="You specialize in identifying productivity bottlenecks and actionable performance insights.",
        verbose=True,
    )


def analyze_productivity(productivity_data: dict) -> dict:
    return {
        "insights": identify_productivity_bottlenecks(productivity_data),
        "completion_rate": productivity_data.get("completion_rate", 0),
    }
