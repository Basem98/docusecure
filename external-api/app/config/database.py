from helpers.singleton import Singleton
from fastapi import HTTPException

class MongoDB(metaclass=Singleton):
    def __init__(self, connection_url, client):
        self._client = client(connection_url)
        
    async def init_db(self, initializer_method, document_models: list[object]):
        await initializer_method(database=self._client.db_name, document_models=document_models)