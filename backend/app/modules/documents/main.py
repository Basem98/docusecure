from boto3 import client
from botocore.config import Config
from .utils.s3_client import S3Client
from config.environment import EnvironmentConfig
from fastapi import APIRouter
from .utils.file_uploader_util import FileUploader
from .services.documents_service import DocumentService
from .controllers.documents_controller import DocumentController
from .database.document_repository import FileRepository
from .models.file_models import File
import httpx

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))


environmentConfig = EnvironmentConfig()
routerInstance = APIRouter()
boto3_client = client(
            service_name='s3',
            aws_access_key_id=environmentConfig.AWS_S3_SECRET_ACCESS_KEY,
            aws_secret_access_key=environmentConfig.AWS_S3_ACCESS_KEY_ID,
            region_name=environmentConfig.AWS_S3_REGION_NAME,
            config=Config({'signature_version': 'v4'})
        )

s3_client = S3Client(boto3_client, environmentConfig.AWS_S3_BUCKET_NAME)
httpx_client = httpx.AsyncClient()
fileUploader = FileUploader(s3_client)
fileRepository = FileRepository(File)
documentService = DocumentService(fileUploader, fileRepository, httpx_client, environmentConfig)
documentController = DocumentController(routerInstance, documentService)
