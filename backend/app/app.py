from fastapi import FastAPI
from helpers.singleton import Singleton


# @Singleton
class App(metaclass=Singleton):
    def __init__(self, FrameworkClass, *args, **kwargs):
        print(FrameworkClass)
        self._app = FrameworkClass(*args, **kwargs)

    def get_app(self):
        return self._app


app = App(FastAPI).get_app()



@app.get("/")
async def root():
    return "Hello, world!"
