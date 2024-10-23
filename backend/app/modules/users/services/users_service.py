from fastapi import HTTPException


class UserService:
    def __init__(self, user_repository, hashing_context, jwt_handler, settings):
        self._settings = settings
        self._user_repository = user_repository
        self._hashing_context = hashing_context
        self._jwt_handler = jwt_handler

    async def register_user(self, user_data):
        user_data['password'] = self._hashing_context.hash(
            user_data['password'])
        result = await self._user_repository.create(user_data)
        return result

    async def login(self, user_data):
        stored_user = await self._user_repository.get_by_user_name(user_data.user_name)
        try:
            print(stored_user)
            if (not stored_user):
                raise HTTPException(status_code=401)
    
            does_password_match = self._hashing_context.verify_hash(
                user_data.password, stored_user.password)
            if (not does_password_match):
                raise HTTPException(status_code=401)
    
            return self._jwt_handler.generate({'user_name': stored_user.user_name, 'role': stored_user.role})
        except Exception as e:
            print(e)
            raise HTTPException(status_code=401, detail="Invalid credentials")
