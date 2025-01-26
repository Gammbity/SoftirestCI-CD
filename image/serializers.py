from image import models
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ['img', 'title', 'created_at']

class ImageRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ['img', 'title', 'description', 'created_at']


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ['user', 'img', 'title', 'description', 'category']