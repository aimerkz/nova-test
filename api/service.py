from api.utils import CreatorFile, CreatorLogs
from gd_service.gd_api import GoogleDriveApi


class UploadService:

    def __init__(self, name: str, data: str):
        self.name = name
        self.data = data

    def execute(self):
        upload_file = CreatorFile(self.name, self.data).create_file()
        GoogleDriveApi().create_file(upload_file.name)
        CreatorLogs(self.name).create_logs_after_upload_file()
