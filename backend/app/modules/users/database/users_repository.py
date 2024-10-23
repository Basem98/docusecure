from modules.users.models.user_models import RegisterUser
from fastapi import HTTPException
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))


class UserRepository:
    def __init__(self, user_model):
        self._user_model = user_model

    async def create(self, user_data):
        try:
            return await self._user_model(**user_data).insert()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="User creation failed")

    async def get_by_user_name(self, user_name):
        try:
            return await self._user_model.find_one(self._user_model.user_name == user_name).project(RegisterUser)
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500, detail="User retrieval failed")
