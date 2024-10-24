from fastapi import HTTPException

class KeywordExtractor:
    def __init__(self, extraction_model):
        self._extraction_model = extraction_model
        
    async def extract(self, document_content):
        try:
            return await self._extraction_model.extract_keywords(document_content)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="keyword extraction failed")