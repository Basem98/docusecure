class DocumentController:
    def __init__(self, Router, *args, **kwargs):
        self._router = Router(*args, **kwargs)
    
    def _establishRoutes(self):
        @self._router.post("/documents", tags=["documents"])
        async def upload_document():
            return {"status": True, "data": {"document": "created"}}
        
    def mountRoutes(self, router_mount_method):
        self._establishRoutes()
        router_mount_method(self._router)