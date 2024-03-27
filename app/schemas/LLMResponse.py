"""Llm Response Schema"""
from pydantic import BaseModel, Field

class LlmPayload(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=255)