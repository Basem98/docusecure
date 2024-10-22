from fastapi import UploadFile
import json

class FileUploader:
    def __init__(self, s3_client):
        self._s3_client = s3_client

    async def upload(self, file: UploadFile):
        file_path = await self._s3_client.upload("sdfvcwfeqw1234234234243", file.filename, file.file)
        return file_path
