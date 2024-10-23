from fastapi import HTTPException


class UserRepository:
    def __init__(self, user_model):
        self._user_model = user_model

    async def create(self, user_data):
        try:
            return await self._user_model(**user_data).insert()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="User creation failed")
