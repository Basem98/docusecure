from beanie import Document, Indexed
from pydantic import BaseModel, Field
from typing import Annotated


class User(Document):
    user_name: Annotated[str, Indexed(unique=True)]
    password: str = Field(exclude=True)
    role: str

    class Settings:
        name = "user"


class RegisterUser(BaseModel):
    user_name: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)


class LoginUser(BaseModel):
    user_name: str = Field(...)
    password: str = Field(...)
