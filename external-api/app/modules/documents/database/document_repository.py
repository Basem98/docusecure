from fastapi import HTTPException

class DocumentMetadataRepository:
    def __init__(self, document_metadata_model):
        self._document_metadata_model = document_metadata_model
        
    async def create_file(self, document_metadata):
        try:
            result = await self._document_metadata_model(**document_metadata).insert()
            return result
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="document metadata creation failed")

    async def search_document(self, search_text):
        try:
            result = await self._document_metadata_model.find({"$text": {"$search": search_text}}).project({"file_path": 1})
            return result
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="document search failed")
