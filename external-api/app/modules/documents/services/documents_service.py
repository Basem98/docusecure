from fastapi import UploadFile, HTTPException
from datetime import datetime
import re

class DocumentService:
    def __init__(self, file_uploader, file_repository, settings):
        self._file_repository = file_repository
        self._file_uploader = file_uploader
        self._settings = settings
        
    async def upload_document(self, file: UploadFile):
        user_id = "123124"
        result = await self._file_uploader.upload(user_id, file)
        file_data = {
            "file_path": result,
            "bucket_name": self._settings.AWS_S3_BUCKET_NAME,
            "file_format": re.findall("(?<=\.)[a-zA-Z]+", file.filename)[0],
            "content_type": file.content_type,
            "file_size": file.size,
            "user_id": user_id,
            "date_created": datetime.now().timestamp(),
            "status": "uploaded",
            "classification": "classified"
        }
        created_file = await self._file_repository.create_file(file_data)
        return {"status": True, "data": created_file}