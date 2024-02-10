from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    ROOT_DIR: Path = Path(__file__).parent.parent.resolve()

    # run server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    # fastapi app
    APP_NAME: str = "App Template"
    APP_ALLOWED_ORIGINS: list[str] = ["*"]
    APP_ALLOWED_HOSTS: list[str] = ["*"]
    DOCS_URL: str | None = None
    REDOC_URL: str | None = None

    # DB settings
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "db"
    DB_HOST: str = "localhost"
    PORT_DB: int = 5432

    # email
    EMAIL_HOST: str = "localhost"
    EMAIL_PORT: int = 465
    EMAIL_USERNAME: str = ""
    EMAIL_PASSWORD: str = ""
    EMAIL_FROM: str = ""
    EMAIL_SUBJECT: str = "Verification email"

    @computed_field
    def database_uri(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:"
            f"{self.DB_PASSWORD}@{self.DB_HOST}:"
            f"{self.PORT_DB}/{self.DB_NAME}"
        )


settings = Config()
