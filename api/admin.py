from django.contrib import admin

from api.models import UploadFile


@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'upload_at')
    list_filter = ('name', )
    ordering = ('upload_at', )
