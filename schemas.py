from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ThreatCategory(str, Enum):
    PHISHING = "phishing"
    BEC = "business_email_compromise"
    DEEPFAKE = "deepfake"
    VOICE_CLONE = "voice_clone"
    DOCUMENT_FORGERY = "document_forgery"
    UNKNOWN = "unknown"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

    @classmethod
    def from_score(cls, score: float):
        if score >= 80:
            return cls.CRITICAL
        if score >= 55:
            return cls.HIGH
        if score >= 25:
            return cls.MEDIUM
        return cls.LOW


class EngineName(str, Enum):
    HEURISTIC = "heuristic_engine"
    LLM = "llm_engine"
    ML_DEEPFAKE = "ml_deepfake_engine"
    ML_VOICE = "ml_voice_clone_engine"


class Signal(BaseModel):
    code: str
    description: str
    weight: float = Field(ge=0, le=100)


class EngineResult(BaseModel):
    engine: EngineName
    score: float = Field(ge=0, le=100)
    signals: list[Signal] = Field(default_factory=list)
    ran: bool = True
    error: Optional[str] = None


class ScanRequest(BaseModel):
    content: str = Field(min_length=1, max_length=50000)
    subject: Optional[str] = None
    sender: Optional[str] = None
    category_hint: Optional[ThreatCategory] = None


class ScanResult(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    category: ThreatCategory
    overall_score: float
    risk_level: RiskLevel
    engine_results: list[EngineResult]
    summary: str
    recommended_action: str