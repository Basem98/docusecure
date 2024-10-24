from beanie import Document
from datetime import datetime

class DocumentMetadata(Document):
    file_id: str
    keywords: list[str]
    date_created: datetime
    date_updated: datetime
    file_path: str
    
    class Settings:
        name = "document_metadata"
        
