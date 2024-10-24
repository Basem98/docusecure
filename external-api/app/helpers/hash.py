from fastapi import HTTPException


class HashingContext:
    def __init__(self, crypt_context, settings):
        self._settings = settings
        self._crypt_context = crypt_context(
            schemes=[self._settings.CRYPT_HASHING_SCHEME], deprecated="auto")

    def hash(self, plain_text):
        try:
            return self._crypt_context.hash(plain_text)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="hashing value failed")

    def verify_hash(self, plain_text, hashed_text):
        try:
            return self._crypt_context.verify(plain_text, hashed_text)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="hashing value failed")
