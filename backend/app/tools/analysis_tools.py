def identify_productivity_bottlenecks(productivity_data: dict) -> list[str]:
    bottlenecks: list[str] = []
    if productivity_data.get("completion_rate", 0) < 60:
        bottlenecks.append("Low task completion rate detected")
    if productivity_data.get("blocked_tasks", 0) > 0:
        bottlenecks.append("Blocked tasks are slowing project progress")
    return bottlenecks


def generate_climate_recommendations(climate_data: dict) -> list[str]:
    recommendations: list[str] = []
    if climate_data.get("engagement_avg", 0) < 6:
        recommendations.append("Run team engagement workshops")
    if climate_data.get("stress_avg", 0) > 7:
        recommendations.append("Introduce workload balancing and wellness interventions")
    if not recommendations:
        recommendations.append("Maintain current climate initiatives and monitor monthly")
    return recommendations


def plan_resource_actions(resource_data: dict) -> list[str]:
    actions: list[str] = []
    if resource_data.get("overloaded_employees"):
        actions.append("Redistribute assignments from overloaded employees")
    if resource_data.get("avg_tasks_per_employee", 0) > 5:
        actions.append("Hire or assign additional support for high-load teams")
    if not actions:
        actions.append("Current allocation is balanced; continue monitoring")
    return actions
