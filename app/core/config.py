from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = False
    secret_key: str
    access_token_expiry_minutes : int = 30
    algorithm: str = "HS256"
    level: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()