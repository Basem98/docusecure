from pydantic_settings import BaseSettings
class EnvironmentConfig(BaseSettings):
    ENVIRONMENT: str
    MAX_FILE_SIZE: str
    ALLOWED_FILE_FORMATS: str
    AWS_S3_ACCESS_KEY_ID: str
    AWS_S3_SECRET_ACCESS_KEY: str
    AWS_S3_BUCKET_NAME: str
    
    class Config:
        env_file = ".env"