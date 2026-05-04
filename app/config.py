from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SERVICE_NAME: str = "coal-monitoring-service"
    ENVIRONMENT: str = "dev"
    SENSOR_DELAY_MIN: float = 0.05
    SENSOR_DELAY_MAX: float = 0.25

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
