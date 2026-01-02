"""
Pydantic models for API request/response serialization
Following C# best practices with strongly-typed models
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


# Request Models
class FraudAnalysisRequest(BaseModel):
    scenario_id: int
    audience: str


class MerchantNarrativeRequest(BaseModel):
    merchant_id: str


class CustomerUpgradeRequest(BaseModel):
    customer_id: str
    output_mode: str = "Executive"
    format_mode: str = "JSON"


class DisputeAnalysisRequest(BaseModel):
    case_id: str


class TestPromptRequest(BaseModel):
    prompt: str


# Response Models
class ScenariosResponse(BaseModel):
    scenarios: List[Dict[str, Any]]
    total: int


class FraudAnalysisResponse(BaseModel):
    scenario: Dict[str, Any]
    analysis: str
    audience: str


class MerchantListResponse(BaseModel):
    merchants: List[Dict[str, Any]]


class MerchantNarrativeResponse(BaseModel):
    success: bool
    narrative: str
    merchant_name: str


class CustomerListResponse(BaseModel):
    customers: List[Dict[str, Any]]


class CustomerUpgradeResponse(BaseModel):
    success: bool
    customer_name: str
    recommendation: str
    output_mode: str
    format_mode: str


class DisputeListResponse(BaseModel):
    disputes: List[Dict[str, Any]]


class DisputeAnalysisResponse(BaseModel):
    success: bool
    case_id: str
    analysis: str


class HeartbeatResponse(BaseModel):
    status: str
    timestamp: str
    message: str


class RootResponse(BaseModel):
    message: str
    status: str
    datetime: str


class TestConnectionResponse(BaseModel):
    success: bool
    message: str
    response: Optional[str] = None
    model: Optional[str] = None
    error: Optional[str] = None


class TestPromptResponse(BaseModel):
    success: bool
    response: str
    model: str
    usage: Dict[str, int]


class ErrorResponse(BaseModel):
    detail: str


# Virtual Agent Models
class AuthenticationRequest(BaseModel):
    code: str


class AuthenticationResponse(BaseModel):
    success: bool
    verified: bool
    customer_name: Optional[str] = None
    account_number: Optional[str] = None
    attempts_remaining: Optional[int] = None
    message: str


class ChatMessage(BaseModel):
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: Optional[str] = None
    sentiment: Optional[str] = None  # 'positive', 'neutral', 'negative', 'frustrated'


class VirtualAgentChatRequest(BaseModel):
    message: str
    conversation_history: List[ChatMessage] = []
    authenticated: bool = False


class VirtualAgentChatResponse(BaseModel):
    response: str
    sentiment: str
    intent: Optional[str] = None
    suggested_actions: List[str] = []
    transfer_to_agent: bool = False
    off_topic_count: int = 0


class CapabilitiesResponse(BaseModel):
    capabilities: List[Dict[str, str]]
    greeting: str
