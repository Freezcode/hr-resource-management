def build_executive_summary(productivity: dict, climate: dict, resources: dict) -> dict:
    return {
        "productivity": productivity,
        "climate": climate,
        "resources": resources,
        "overall_status": "attention_needed"
        if productivity.get("completion_rate", 0) < 70 or climate.get("stress_avg", 0) > 7
        else "healthy",
    }
