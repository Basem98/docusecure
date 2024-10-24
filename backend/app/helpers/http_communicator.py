

class HttpClient:
    def __init__(self, http_client):
        self._http_client = http_client
    
    async def get(self, api_url, *args, **kwargs):
        async with self._http_client as client:
            response = await client.get(api_url, *args, **kwargs)
            return response.json()
        
        
    async def post(self, api_url, body, files, *args, **kwargs):
        async with self._http_client as client:
            response = await client.post(api_url, data=body, files=files)
            return response.json()