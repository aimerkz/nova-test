import re
from collections import OrderedDict

from rest_framework import serializers

from api.models import UploadFile


class UploadFileSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=1, max_length=100)
    data = serializers.CharField(required=True, min_length=1)

    class Meta:
        fields = ('name', 'data')

    def validate(self, attrs):
        name = attrs.get('name')
        if not re.search('.txt', name):
            raise serializers.ValidationError()
        return attrs


class UploadFileLogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    upload_at = serializers.DateTimeField(read_only=True)
    name = serializers.CharField(required=True, min_length=1, max_length=100)

    class Meta:
        model = UploadFile
        fields = ('id', 'name', 'upload_at')

    def create(self, validated_data: OrderedDict):
        """Создание записи в бд о загрузке файла на гугл диск"""
        return UploadFile.objects.create(**validated_data)
