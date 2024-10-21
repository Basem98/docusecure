from .controllers.documents_controller import DocumentController
from fastapi import APIRouter


documentController = DocumentController(APIRouter)