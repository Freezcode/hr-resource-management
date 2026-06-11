"""HR program to measure productivity, work climate, and environment."""

from __future__ import annotations


def _validate_score(name: str, value: float) -> float:
    if not 0 <= value <= 100:
        raise ValueError(f"{name} must be between 0 and 100.")
    return value


def evaluate_hr_metrics(
    productivity: float, work_climate: float, work_environment: float
) -> dict[str, object]:
    productivity = _validate_score("productivity", productivity)
    work_climate = _validate_score("work_climate", work_climate)
    work_environment = _validate_score("work_environment", work_environment)

    overall_score = round((productivity + work_climate + work_environment) / 3, 2)

    if overall_score >= 85:
        rating = "Excellent"
    elif overall_score >= 70:
        rating = "Good"
    elif overall_score >= 50:
        rating = "Average"
    else:
        rating = "Needs Improvement"

    focus_areas = []
    if productivity < 70:
        focus_areas.append("Productivity")
    if work_climate < 70:
        focus_areas.append("Work climate")
    if work_environment < 70:
        focus_areas.append("Work environment")

    if not focus_areas:
        focus_areas.append("Maintain current standards")

    return {
        "overall_score": overall_score,
        "rating": rating,
        "focus_areas": focus_areas,
    }


def _read_score(label: str) -> float:
    return float(input(f"Enter {label} score (0-100): ").strip())


def main() -> None:
    productivity = _read_score("productivity")
    work_climate = _read_score("work climate")
    work_environment = _read_score("work environment")

    report = evaluate_hr_metrics(productivity, work_climate, work_environment)

    print("\nHR Assessment Report")
    print(f"Overall Score: {report['overall_score']}")
    print(f"Rating: {report['rating']}")
    print("Focus Areas:")
    for area in report["focus_areas"]:
        print(f"- {area}")


if __name__ == "__main__":
    main()
