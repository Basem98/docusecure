from pydantic_settings import BaseSettings


class EnvironmentConfig(BaseSettings):
    ENVIRONMENT: str

    AWS_S3_ACCESS_KEY_ID: str
    AWS_S3_SECRET_ACCESS_KEY: str
    AWS_S3_BUCKET_NAME: str
    AWS_S3_REGION_NAME: str

    DB_CONNECTIORN_URL: str

    class Config:
        env_file = ".env"
