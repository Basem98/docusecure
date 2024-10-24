from fastapi import UploadFile, HTTPException
from datetime import datetime
import re


class DocumentService:
    def __init__(self, document_metadata_repository, keyword_extractor, settings):
        self._document_metadata_repository = document_metadata_repository
        self._settings = settings
        self._keyword_extractor = keyword_extractor

    async def extract_document_metadata(self, file: UploadFile, file_path):
        try:
            # 1. Read file content
            file_content = await file.read()
            # 2. Extract keywords from file
            document_metadata = {
                'data_created': datetime.now().timestamp(),
                'data_updated': datetime.now().timestamp(),
                'keywords': await self._keyword_extractor.extract(file_content),
                'file_path': file_path,
                'file_content': file_content
            }
            print(document_metadata.keywords)
            # 3. Store the keywords along with other metadata and file_path into db
            await self._document_metadata_repository.create(document_metadata)
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500, detail="Document metadata extraction failed")

    async def search_document_content(self, search_text):
        return self._document_metadata_repository.search_document(search_text)