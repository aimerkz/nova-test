import os
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from backend.settings import FOLDER_ID, FOLDER_NAME

# Находим файл с кредами для работы с Google Drive Api
SCOPES = ['https://www.googleapis.com/auth/drive']
CREDS_PATH = 'creds.json'
SERVICE_ACCOUNT_FILE = os.path.abspath(CREDS_PATH)

# Загружаем креды для работы сервиса
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Создаем экземпляр сервиса для взаимодействия с Google Drive Api
drive_service = build('drive', 'v3', credentials=credentials)


class GoogleDriveApi:

    def create_folder(self):
        """Создание папки внутри существующей Test Upload"""

        folder_metadata = {
            'name': FOLDER_NAME,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [FOLDER_ID]
        }

        created_folder = drive_service.files().create(
            body=folder_metadata,
        ).execute()
        return created_folder

    def create_file(self, name: str):
        """
        Добавление файла в папку Test Upload
        """
        file_metadata = {'name': Path(name).name, 'parents': [FOLDER_ID]}
        media = MediaFileUpload(filename=name,
                                mimetype='text/plain')
        file = drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        return file
