from fastapi import UploadFile, HTTPException

class DocumentService:
    def __init__(self, file_uploader):
        self.file_uploader = file_uploader
        
    async def upload_document(self, file: UploadFile):
        result = await self.file_uploader.upload(file)
        return {"status": True, "data": result}