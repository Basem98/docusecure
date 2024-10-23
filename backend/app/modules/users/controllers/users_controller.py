from fastapi import UploadFile, File

class UserController:
    def __init__(self, framework_router, userService):
        self._router = framework_router
        self._userService = userService
    
    def _establishRoutes(self):
        @self._router.post("/users", tags=["users"])
        async def register():
            pass
        
    def mountRoutes(self, router_mount_method):
        self._establishRoutes()
        router_mount_method(self._router)