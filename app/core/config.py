from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = False
    secret_key: str
    access_token: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()