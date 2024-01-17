from django.urls import path

from api.views import UploadFileView

app_name = 'api'

urlpatterns = [
    path(
        '',
        UploadFileView.as_view(),
        name='upload_file',
    )
]
