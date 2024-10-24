from beanie import Document, Indexed
from datetime import datetime
from typing import Annotated
from pydantic import BaseModel
import pymongo

class DocumentMetadata(Document):
    date_created: datetime
    date_updated: datetime
    file_path: str
    file_content: Annotated[str, Indexed(index_type=pymongo.TEXT)]
    
    class Settings:
        name = "document_metadata"
        
        
        
        
class DocumentSearchResult(BaseModel):
    file_path: str