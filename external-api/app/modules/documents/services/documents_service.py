from fastapi import UploadFile, HTTPException
from datetime import datetime
import re


class DocumentService:
    def __init__(self, document_metadata_repository, settings):
        self._document_metadata_repository = document_metadata_repository
        self._settings = settings

    async def extract_document_metadata(self, file_content, file_path):
        try:
            # 1. Read file content
            # 2. Extract keywords from file
            document_metadata = {
                'date_created': datetime.now().timestamp(),
                'date_updated': datetime.now().timestamp(),
                'file_path': file_path,
                'file_content': file_content,
                
            }
            # 3. Store the keywords along with other metadata and file_path into db
            return await self._document_metadata_repository.create(document_metadata)
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500, detail="Document metadata extraction failed")

    async def search_document_content(self, search_text):
        try:
            result = await self._document_metadata_repository.search_document(search_text)
            files_paths = [];
            for path in result:
                files_paths.append(path.file_path)
            return files_paths
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="document search failure")