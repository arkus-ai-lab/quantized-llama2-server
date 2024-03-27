from fastapi import APIRouter, Request
from controllers.llm_controller import LlmResponseController

router = APIRouter()
llm_controller = LlmResponseController('merged_adapters/ggml-model-q8_0.gguf')

@router.post("/llm/")
async def create_llm(request: Request):
    payload = await request.body()
    decoded_payload = payload.decode('utf-8')
    json_payload = eval(decoded_payload)['prompt']

    response = llm_controller.generate_text(json_payload)
    return response