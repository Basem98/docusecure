import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from fastapi import HTTPException
from datetime import datetime
from helpers.singleton import Singleton
import boto3
from botocore.config import Config


class S3Client(metaclass=Singleton):
    def __init__(self, s3_client, bucket_name):
        self._bucket_name = bucket_name
        self._client = s3_client
        
    async def upload(self, folder_name, file_name, file):
        try:
            file_path = f'{folder_name}/{datetime.now().timestamp()
                                         }-{file_name}'
            self._client.upload_fileobj(file, self._bucket_name, file_path)
            return file_path
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="File upload failed")
    
    def generate_s3_url(self, file_path):
        try:
            url = self._client.generate_presigned_url(
                "get_object", {"Bucket": self._bucket_name, "Key": file_path}, ExpiresIn=3600)
            return url
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="File upload failed")
