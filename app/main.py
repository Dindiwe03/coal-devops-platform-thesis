from fastapi import FastAPI
from app.api.routes import router
from app.config import settings

app = FastAPI(
    title="Coal Industry DevOps Monitoring Platform",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "service": settings.SERVICE_NAME,
        "environment": settings.ENVIRONMENT
    }
