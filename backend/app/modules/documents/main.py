from boto3 import client
from botocore.config import Config
from .utils.s3_client import S3Client
from config.environment import EnvironmentConfig
from fastapi import APIRouter
from .utils.file_uploader_util import FileUploader
from .services.documents_service import DocumentService
from .controllers.documents_controller import DocumentController
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))


environmentConfig = EnvironmentConfig()
routerInstance = APIRouter()
print(environmentConfig)
s3_client = S3Client(client, environmentConfig.AWS_S3_BUCKET_NAME,
                     environmentConfig.AWS_S3_SECRET_ACCESS_KEY, environmentConfig.AWS_S3_ACCESS_KEY_ID, environmentConfig.AWS_S3_REGION_NAME, Config({'signature_version': 'v4'}))
fileUploader = FileUploader(s3_client)
documentService = DocumentService(fileUploader)
documentController = DocumentController(routerInstance, documentService)
