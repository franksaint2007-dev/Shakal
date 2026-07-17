from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
    title="AI Scam Shield API",
    version="1.0"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "service":"AI Scam Shield",
        "status":"running"
    }