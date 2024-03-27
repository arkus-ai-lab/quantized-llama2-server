from fastapi import FastAPI
from router.llm_routing import router as llm_router
from router.index_routing import router as index_router

app = FastAPI()

app.include_router(llm_router, prefix="/api")
app.include_router(index_router)