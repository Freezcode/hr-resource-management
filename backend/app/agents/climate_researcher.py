from typing import Any

from app.tools.analysis_tools import generate_climate_recommendations

try:
    from crewai import Agent
except Exception:
    Agent = None


def build_climate_researcher_agent() -> Any:
    if Agent is None:
        return {
            "role": "Climate Researcher",
            "goal": "Assess employee engagement and workplace environment",
        }

    return Agent(
        role="Climate Researcher",
        goal="Analyze employee survey responses and workplace climate indicators",
        backstory="You uncover trends in engagement, stress, and sentiment to improve team climate.",
        verbose=True,
    )


def analyze_climate(climate_data: dict) -> dict:
    return {
        "recommendations": generate_climate_recommendations(climate_data),
        "engagement_avg": climate_data.get("engagement_avg", 0),
        "stress_avg": climate_data.get("stress_avg", 0),
    }
