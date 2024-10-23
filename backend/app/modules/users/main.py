import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from fastapi import APIRouter
from passlib.context import CryptContext
from config.environment import EnvironmentConfig
from .controllers.users_controller import UserController
from .services.users_service import UserService
from .database.users_repository import UserRepository
from .models.user_models import User
from helpers.hash import HashingContext

environmentConfig = EnvironmentConfig()
routerInstance = APIRouter()

hashingContext = HashingContext(CryptContext, environmentConfig)
userRepository = UserRepository(User)
userService = UserService(userRepository, hashingContext, environmentConfig)
userController = UserController(routerInstance, userService)
