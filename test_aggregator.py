from app.core.aggregator import combine
from app.core.schemas import (
    EngineName,
    EngineResult,
    RiskLevel,
    Signal,
    ThreatCategory,
)


def test_combines_weighted_scores():

    heuristic = EngineResult(
        engine=EngineName.HEURISTIC,
        score=40.0,
        signals=[],
        ran=True
    )

    llm = EngineResult(
        engine=EngineName.LLM,
        score=80.0,
        signals=[],
        ran=True
    )

    result = combine(
        [heuristic, llm],
        category=ThreatCategory.PHISHING
    )

    assert result.overall_score == 64.0
    assert result.risk_level == RiskLevel.HIGH



def test_single_engine_ran_uses_score():

    heuristic = EngineResult(
        engine=EngineName.HEURISTIC,
        score=30.0,
        signals=[],
        ran=True
    )

    llm = EngineResult(
        engine=EngineName.LLM,
        score=0,
        signals=[],
        ran=False,
        error="no API key"
    )

    result = combine(
        [heuristic, llm],
        category=ThreatCategory.PHISHING
    )

    assert result.overall_score == 30.0



def test_no_engines_is_not_safe():

    heuristic = EngineResult(
        engine=EngineName.HEURISTIC,
        score=0,
        signals=[],
        ran=False,
        error="failed"
    )

    result = combine(
        [heuristic],
        category=ThreatCategory.PHISHING
    )

    assert "NOT" in result.summary