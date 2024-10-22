class FileRepository:
    def __init__(self, file_model):
        print(file_model)
        self._file_model = file_model
    async def create_file(self, fileData):
        result = await self._file_model(fileData).insert()
        return result