from fastapi import UploadFile, File

class DocumentController:
    def __init__(self, framework_router, documentService):
        self._router = framework_router
        self._documentService = documentService
    
    def _establishRoutes(self):
        @self._router.post("/documents", tags=["documents"])
        async def upload_document(file: UploadFile = File(...)):
            result = await self._documentService.upload_document(file)
            return result
        
    def mountRoutes(self, router_mount_method):
        self._establishRoutes()
        router_mount_method(self._router)