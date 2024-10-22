from beanie import Document
from datetime import datetime

class File(Document):
    user_id: str
    file_size: float
    file_type: str
    bucket_name: str
    date_created: datetime
    status: str
    classification: str
    file_path: str

    class Settings:
        name = 'file'
        
