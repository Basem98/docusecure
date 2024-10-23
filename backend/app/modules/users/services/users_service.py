from fastapi import HTTPException


class UserService:
    def __init__(self, user_repository, hashing_context, settings):
        self._settings = settings
        self._user_repository = user_repository
        self._hashing_context = hashing_context

    async def register_user(self, user_data):
        user_data['password'] = self._hashing_context.hash(
            user_data['password'])
        result = await self._user_repository.create(user_data)
        return result
