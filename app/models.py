from pydantic import BaseModel
from enum import Enum


class SensorStatus(str, Enum):
    OK = "ok"
    WARNING = "warning"
    CRITICAL = "critical"


class SensorData(BaseModel):
    temperature: float
    vibration: float
    gas_level: float
    status: SensorStatus
