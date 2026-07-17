from app.core.schemas import (
    EngineName,
    EngineResult,
)


def analyze_deepfake(file_path):

    return EngineResult(
        engine=EngineName.ML_DEEPFAKE,
        score=0,
        signals=[],
        ran=False,
        error="Deepfake model not trained yet"
    )


def analyze_voice_clone(file_path):

    return EngineResult(
        engine=EngineName.ML_VOICE,
        score=0,
        signals=[],
        ran=False,
        error="Voice clone model not trained yet"
    )