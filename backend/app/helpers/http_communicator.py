

class HttpClient:
    def __init__(self, http_client):
        self._http_client = http_client
    
    async def get(self, api_url):
        async with self._http_client() as client:
            response = await client.get(api_url)
            return response.json()
        
        
    async def post(self, api_url, data):
        print(api_url)
        async with self._http_client() as client:
            response = await client.post(api_url, json=data)
            return response.json()