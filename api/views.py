from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from api.models import UploadFile
from api.serializers import UploadFileLogSerializer, UploadFileSerializer
from api.service import UploadService


class UploadFileView(ListCreateAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileLogSerializer

    @extend_schema(tags=['upload-file'])
    def get(self, request: Request, *args, **kwargs) -> Response:
        """Получение записей о загрузке файлов в Google Drive"""

        return super().get(self, request, *args, **kwargs)

    @extend_schema(
        tags=['upload-file'],
        request=UploadFileSerializer,
        description='param: name - имя файла.формат (к примеру, file.txt)  \n'
                    'param: data - текстовое содержимое будущего файла (str type)',
        responses={HTTP_201_CREATED: OpenApiResponse()}
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Загрузка файла в Google Drive"""

        serializer = UploadFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.pop('name')
        data = serializer.validated_data.pop('data')
        UploadService(name, data).execute()
        return Response(status=HTTP_201_CREATED, data='Файл успешно загружен в Google Drive')
