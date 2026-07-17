from app.core.schemas import (
    EngineName,
    EngineResult,
    RiskLevel,
    ScanResult,
    ThreatCategory,
)


_ENGINE_WEIGHTS = {
    EngineName.HEURISTIC: 0.4,
    EngineName.LLM: 0.6,
}


_ACTION_BY_RISK = {
    RiskLevel.LOW:
        "No action needed. Continue normal handling.",

    RiskLevel.MEDIUM:
        "Review manually before acting.",

    RiskLevel.HIGH:
        "Do not act. Verify sender identity separately.",

    RiskLevel.CRITICAL:
        "Block and report immediately.",
}


def combine(
    engine_results: list[EngineResult],
    category: ThreatCategory = ThreatCategory.UNKNOWN,
):

    active = [x for x in engine_results if x.ran]

    if not active:
        score = 0.0
        summary = (
            "No detection engine could run. "
            "This should NOT be treated as safe."
        )

    else:
        total_weight = sum(
            _ENGINE_WEIGHTS.get(x.engine, 1)
            for x in active
        )

        score = sum(
            x.score * _ENGINE_WEIGHTS.get(x.engine, 1)
            for x in active
        ) / total_weight

        signals = sorted(
            [
                s
                for e in active
                for s in e.signals
            ],
            key=lambda x: x.weight,
            reverse=True
        )[:3]

        summary = (
            "Key indicators: "
            + "; ".join(
                s.description for s in signals
            )
        ) if signals else "No scam indicators detected."

    risk = RiskLevel.from_score(score)

    return ScanResult(
        category=category,
        overall_score=round(score, 1),
        risk_level=risk,
        engine_results=engine_results,
        summary=summary,
        recommended_action=_ACTION_BY_RISK[risk],
    )