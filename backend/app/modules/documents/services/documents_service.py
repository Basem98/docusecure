from fastapi import UploadFile, HTTPException
from datetime import datetime

class DocumentService:
    def __init__(self, file_uploader, file_repository, settings):
        self._file_repository = file_repository
        self._file_uploader = file_uploader
        self._settings = settings
        
    async def upload_document(self, file: UploadFile):
        result = await self._file_uploader.upload(file)
        file_data = {
            "file_path": result,
            "bucket_name": self._settings.AWS_S3_BUCKET_NAME,
            "file_type": file.content_type,
            "file_size": file.size,
            "user_id": "123124",
            "date_created": datetime.now().timestamp(),
            "status": "uploaded",
            "classification": "classified"
        }
        created_file = await self._file_repository.create_file(file_data)
        return {"status": True, "data": created_file}