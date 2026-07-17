import re

from app.core.schemas import (
    EngineName,
    EngineResult,
    Signal,
)


URGENCY = [
    r"\burgent\b",
    r"\bimmediately\b",
    r"\bwithin \d+ hours\b",
]

PAYMENT = [
    r"change bank details",
    r"wire transfer",
    r"send payment",
]

CREDENTIALS = [
    r"verify your password",
    r"enter your credentials",
]


def analyze(
    content: str,
    subject=None,
    sender=None
):

    text = f"{subject or ''}\n{content}"

    signals = []

    for pattern in URGENCY:
        if re.search(pattern, text, re.I):
            signals.append(
                Signal(
                    code="URGENCY_LANGUAGE",
                    description="Urgency language detected",
                    weight=15
                )
            )
            break


    for pattern in PAYMENT:
        if re.search(pattern, text, re.I):
            signals.append(
                Signal(
                    code="PAYMENT_REDIRECT_REQUEST",
                    description="Payment change request detected",
                    weight=35
                )
            )
            break


    for pattern in CREDENTIALS:
        if re.search(pattern, text, re.I):
            signals.append(
                Signal(
                    code="CREDENTIAL_HARVEST_PATTERN",
                    description="Credential theft attempt detected",
                    weight=20
                )
            )
            break


    score = min(
        100,
        sum(x.weight for x in signals)
    )


    return EngineResult(
        engine=EngineName.HEURISTIC,
        score=score,
        signals=signals,
        ran=True
    )