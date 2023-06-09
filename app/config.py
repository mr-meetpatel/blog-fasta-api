from pydantic import BaseSettings


class Settings(BaseSettings):
    DRIVER: str
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ORIGINS: str

    class Config:
        env_file = ".env"


settings = Settings()
