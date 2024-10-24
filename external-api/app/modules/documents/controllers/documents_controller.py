from fastapi import UploadFile, File

class DocumentController:
    def __init__(self, framework_router, documentService):
        self._router = framework_router
        self._documentService = documentService
    
    def _establishRoutes(self):
        @self._router.post("/documents", tags=["documents"])
        async def extract_document_metadata(file: UploadFile = File(...)):
            result = await self._documentService.extract_document_metadata(file)
            return result
        
        @self._router.post("/documents/search", tags=["documents"])
        async def searchDocumentMetadata(text: str):
            return self._documentService.search_documentI(text)

    def mountRoutes(self, router_mount_method):
        self._establishRoutes()
        router_mount_method(self._router)