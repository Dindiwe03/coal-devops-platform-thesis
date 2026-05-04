import random
import time
from app.config import settings
from app.models import SensorData, SensorStatus


def generate_sensor_data() -> SensorData:
    time.sleep(random.uniform(
        settings.SENSOR_DELAY_MIN,
        settings.SENSOR_DELAY_MAX
    ))

    temperature = random.uniform(40, 95)
    vibration = random.uniform(0.1, 3.0)
    gas = random.uniform(0, 100)

    if temperature > 85 or gas > 80:
        status = SensorStatus.CRITICAL
    elif temperature > 70:
        status = SensorStatus.WARNING
    else:
        status = SensorStatus.OK

    return SensorData(
        temperature=round(temperature, 2),
        vibration=round(vibration, 2),
        gas_level=round(gas, 2),
        status=status
    )
