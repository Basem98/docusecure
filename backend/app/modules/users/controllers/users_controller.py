from fastapi import UploadFile, File, Body
from ..models.user_models import RegisterUser


class UserController:
    def __init__(self, framework_router, user_service):
        self._router = framework_router
        self._user_service = user_service

    def _establishRoutes(self):
        @self._router.post("/users", tags=["users"])
        async def register_user(user_data: RegisterUser = Body(...)):
            print(user_data)
            return await self._user_service.register_user(user_data.dict())

    def mountRoutes(self, router_mount_method):
        self._establishRoutes()
        router_mount_method(self._router)
