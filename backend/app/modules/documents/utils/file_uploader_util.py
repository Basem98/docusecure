from fastapi import UploadFile
import json

class FileUploader:
    def __init__(self, s3_client):
        self._s3_client = s3_client

    async def upload(self, user_id, file: UploadFile):
        file_path = await self._s3_client.upload(user_id, file.filename, file.file)
        return file_path
