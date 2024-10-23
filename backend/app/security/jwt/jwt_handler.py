from fastapi import HTTPException

class JWT_Handler:
    def __init__(self, jwt_module, jwt_secret, jwt_expiry, jwt_algorithm):
        self._jwt_secret = jwt_secret
        self._jwt_expiry = jwt_expiry
        self._jwt_algorithm = jwt_algorithm
        self._jwt_module = jwt_module
        
    
    def generate(self, payload):
        return self._jwt_module.encode(payload, self._jwt_secret, algorithm=self._jwt_algorithm)
    
    def decode(self, token):
        try:
            return self._jwt_module.decode(token, self._jwt_secret, algorithm=self._jwt_algorithm)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=401, detail="Invalid auth token")