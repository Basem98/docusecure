from .controllers.documents_controller import DocumentController
from fastapi import APIRouter

routerInstance = APIRouter()
documentController = DocumentController(routerInstance)