from django.core.files import File

from api.models import UploadFile

FILES_FOLDER: str = 'files_uploaded/'


class CreatorFile:

    def __init__(self, name: str, data: str):
        self.name = name
        self.data = data

    def create_file(self) -> File:
        """Создание файла на основе переданных name и data"""
        res = open(FILES_FOLDER + self.name, 'w')  # noqa: SIM115
        res.write(self.data)
        res.close()
        return File(res)


class CreatorLogs:

    def __init__(self, name: str):
        self.name = name

    def create_logs_after_upload_file(self) -> UploadFile:
        """Создание записи в бд о загрузке файла в Google Drive"""
        return UploadFile.objects.create(name=self.name)
