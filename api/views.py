from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from api.models import UploadFile
from api.serializers import UploadFileLogSerializer, UploadFileSerializer
from api.utils import CreatorFile
from gd_service.gd_api import GoogleDriveApi


class UploadFileView(ListCreateAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileLogSerializer

    @extend_schema(tags=['upload-file'])
    def get(self, request: Request, *args, **kwargs) -> Response:
        """Получение записей о загрузке файлов на гугл диск"""

        return super().get(self, request, *args, **kwargs)

    @extend_schema(tags=['upload-file'], request=UploadFileSerializer)
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Загрузка файла на гугл диск"""

        serializer = UploadFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.pop('name')
        data = serializer.validated_data.pop('data')
        upload_file = CreatorFile(name, data).create_file()
        GoogleDriveApi().create_file(upload_file.name)
        return Response(status=HTTP_201_CREATED, data='Файл успешно загружен в Google Drive')
