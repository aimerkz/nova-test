from django.db import models


class UploadFile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя файла', null=False, blank=False, max_length=100)
    upload_at = models.DateTimeField(verbose_name='Дата добавления файла', auto_now_add=True)

    objects = models.Manager()
