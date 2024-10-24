from boto3 import client
from botocore.config import Config
from .utils.s3_client import S3Client
from config.environment import EnvironmentConfig
from fastapi import APIRouter
from .services.documents_service import DocumentService
from .controllers.documents_controller import DocumentController
from .database.document_repository import DocumentMetadataRepository
from .models.file_models import File
from helpers.keyword_extractor import KeywordExtractor
from keybert import KeyBERT
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))


environmentConfig = EnvironmentConfig()
routerInstance = APIRouter()
s3_client = S3Client(client, environmentConfig.AWS_S3_BUCKET_NAME,
                     environmentConfig.AWS_S3_SECRET_ACCESS_KEY, environmentConfig.AWS_S3_ACCESS_KEY_ID, environmentConfig.AWS_S3_REGION_NAME, Config({'signature_version': 'v4'}))
document_metadata_repository = DocumentMetadataRepository(File)
keybert_model = KeyBERT(environmentConfig.KEYBERT_EXTRACTION_MODEL)
document_keyword_extractor = KeywordExtractor(keybert_model)
documentService = DocumentService(document_metadata_repository, document_keyword_extractor, environmentConfig)
documentController = DocumentController(routerInstance, documentService)
