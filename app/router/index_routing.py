from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/")
async def root():
    return {
        "version": "0.1.0",
        "description": "Kwaai - Quantized LLM API",
        "name": "Kwaai - Quantized LLM API",
        "routes": {
            "llm": "/api/llm/",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }