import jwt
from security.jwt.jwt_handler import JWT_Handler
from helpers.hash import HashingContext
from .models.user_models import User
from .database.users_repository import UserRepository
from .services.users_service import UserService
from .controllers.users_controller import UserController
from config.environment import EnvironmentConfig
from passlib.context import CryptContext
from fastapi import APIRouter
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))


environmentConfig = EnvironmentConfig()
routerInstance = APIRouter()

hashingContext = HashingContext(CryptContext, environmentConfig)
jwtHandler = JWT_Handler(jwt, environmentConfig.JWT_SECRET_KEY,
                         environmentConfig.JWT_EXPIRY_TIME_IN_MINUTES, environmentConfig.JWT_ALGORITHM)
userRepository = UserRepository(User)
userService = UserService(userRepository, hashingContext,
                          jwtHandler, environmentConfig)
userController = UserController(routerInstance, userService)
