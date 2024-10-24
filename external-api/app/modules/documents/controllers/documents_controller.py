from fastapi import UploadFile, File, Form
from models.document_models import DocumentMetadataExtractionBody
class DocumentController:
    def __init__(self, framework_router, documentService):
        self._router = framework_router
        self._documentService = documentService
    
    def _establishRoutes(self):
        @self._router.post("/documents", tags=["documents"])
        # async def extract_document_metadata(file: UploadFile = File(...), filce_path: str = Form()):
        async def extract_document_metadata(body: DocumentMetadataExtractionBody):
            result = await self._documentService.extract_document_metadata(body.file_content, body.file_path)
            return result
        
        @self._router.get("/documents/search", tags=["documents"])
        async def searchDocumentMetadata(text: str):
            try:
                return await self._documentService.search_document_content(text)
            except Exception as e:
                print(e)

    def mountRoutes(self, router_mount_method):
        self._establishRoutes()
        router_mount_method(self._router)