from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Livlong Health AI"
    API_V1_STR: str = "/api/v1"
    OPENAI_API_KEY: str  # Required
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()