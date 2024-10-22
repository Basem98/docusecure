from beanie import Document
from datetime import datetime

class DocumentMetadata(Document):
    file_id: str
    keywords: list[str]
    date_created: datetime.timestamp
    date_updated: datetime.timestamp
    file_path: str
    
    class Settings:
        name = "document_metadata"
        
