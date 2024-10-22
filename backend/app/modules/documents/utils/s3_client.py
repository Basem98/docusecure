import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from helpers.singleton import Singleton
from datetime import datetime
from fastapi import HTTPException

class S3Client(metaclass=Singleton):
    def __init__(self, s3_client, bucket_name, aws_secret_access_key, aws_access_key_id):
        self._bucket_name = bucket_name
        self._aws_secret_access_key = aws_secret_access_key
        self._aws_access_key_id = aws_access_key_id
        self._client = s3_client(
            service_name='s3',
            aws_access_key_id=self._aws_access_key_id,
            aws_secret_access_key=self._aws_secret_access_key)
        
    async def upload(self, folder_name, file_name, file):
        try:
            file_path = f'{folder_name}/{file_name}-{datetime.now()}'
            await self._client.upload_fileobj(file, self._bucket_name, file_path)
            return file_path
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="File upload failed")