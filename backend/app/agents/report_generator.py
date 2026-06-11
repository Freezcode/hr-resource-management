from typing import Any

from app.tools.report_tools import build_executive_summary

try:
    from crewai import Agent
except Exception:
    Agent = None


def build_report_generator_agent() -> Any:
    if Agent is None:
        return {
            "role": "Report Generator",
            "goal": "Synthesize all agent insights into clear reports",
        }

    return Agent(
        role="Report Generator",
        goal="Create dashboards, summaries, and actionable recommendations",
        backstory="You convert complex analytics into concise executive and team reports.",
        verbose=True,
    )


def generate_report(productivity: dict, climate: dict, resources: dict) -> dict:
    return build_executive_summary(productivity, climate, resources)
