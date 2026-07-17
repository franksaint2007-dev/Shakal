import os
import json

from anthropic import Anthropic

from app.core.schemas import (
    EngineName,
    EngineResult,
    Signal,
)


def analyze(content):

    key = os.getenv(
        "ANTHROPIC_API_KEY"
    )

    if not key:
        return EngineResult(
            engine=EngineName.LLM,
            score=0,
            signals=[],
            ran=False,
            error="Missing API key"
        )


    client = Anthropic(api_key=key)


    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[
            {
                "role":"user",
                "content":
                f"Analyze scam risk:\n{content}"
            }
        ]
    )


    return EngineResult(
        engine=EngineName.LLM,
        score=0,
        signals=[],
        ran=True
    )