from fastapi import APIRouter
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

from app.metrics import REQUEST_COUNTER, REQUEST_LATENCY, ACTIVE_ALERTS
from app.services.sensor_service import generate_sensor_data

router = APIRouter()


@router.get("/sensor")
def read_sensor():
    REQUEST_COUNTER.inc()

    with REQUEST_LATENCY.time():
        data = generate_sensor_data()

    if data.status == "critical":
        ACTIVE_ALERTS.inc()

    return data


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
