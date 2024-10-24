from beanie import Document, Indexed
from datetime import datetime
from typing import Annotated
import pymongo

class DocumentMetadata(Document):
    file_id: str
    keywords: list[str]
    date_created: datetime
    date_updated: datetime
    file_path: str
    file_content: Annotated[str, Indexed(index_type=pymongo.TEXT)]
    
    class Settings:
        name = "document_metadata"
        
