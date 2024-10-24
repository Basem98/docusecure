from fastapi import UploadFile, HTTPException
from datetime import datetime
import re


class DocumentService:
    def __init__(self, file_uploader, file_repository, http_client, settings):
        self._file_repository = file_repository
        self._file_uploader = file_uploader
        self._settings = settings
        self._http_client = http_client

    async def upload_document(self, file: UploadFile):
        try:
            user_id = "123124"
            file_content = file.file
            result = await self._file_uploader.upload(user_id, file_content, file.filename)
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
            metadata_storage_result = await self._http_client.post(f"{self._settings.METADATA_API_URL}/documents", {"file_path": result, "file_content": file_content})
            print(metadata_storage_result)
            return {"status": True, "data": created_file}
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500, detail="document upload failed")
