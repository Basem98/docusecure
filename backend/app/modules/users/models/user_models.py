from beanie import Document

class UserModel(Document):
    user_name: str
    email: str
    password: str
    role: str

    class Settings:
        "name" = "user"