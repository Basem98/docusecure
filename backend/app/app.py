from fastapi import FastAPI
from helpers.singleton import Singleton
from modules.documents.main import documentController


class App(metaclass=Singleton):
    def __init__(self, FrameworkClass, *args, **kwargs):
        self._app = FrameworkClass(*args, **kwargs)

    def get_app(self):
        return self._app
    
    def init_controllers(self, controllers):
        for controller in controllers:
            controller.mountRoutes(self._app.include_router)
        

appWrapper = App(FastAPI)

app = appWrapper.get_app()

appWrapper.init_controllers([documentController])


