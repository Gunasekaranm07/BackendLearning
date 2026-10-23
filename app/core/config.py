from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = False

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()