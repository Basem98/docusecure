from fastapi import FastAPI, HTTPException
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.singleton import Singleton
from modules.documents.main import documentController
from modules.users.main import userController
from modules.documents.models.document_models import DocumentMetadata
from modules.documents.models.file_models import File
from modules.users.models.user_models import User
from config.database import MongoDB
from config.environment import EnvironmentConfig


class App(metaclass=Singleton):
    def __init__(self, FrameworkClass, *args, **kwargs):
        self._app = FrameworkClass(*args, **kwargs)

    def get_app(self):
        return self._app

    def init_controllers(self, controllers):
        for controller in controllers:
            controller.mountRoutes(self._app.include_router)

    async def init_db(self, db_connector_instance, initializer_method, db_models):
        await db_connector_instance.init_db(initializer_method, db_models)


environmentConfig = EnvironmentConfig()
appWrapper = App(FastAPI)

app = appWrapper.get_app()

appWrapper.init_controllers([documentController, userController])


@app.on_event("startup")
async def start_up():
    await appWrapper.init_db(MongoDB(environmentConfig.DB_CONNECTIORN_URL, AsyncIOMotorClient), init_beanie, [DocumentMetadata, File, User])
