from rest_framework import generics
from image import models, serializers
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

class ImageListView(generics.ListAPIView):
    serializer_class = serializers.ImageSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category:    
            return models.Image.objects.filter(category=category).order_by('-created_at')
        return models.Image.objects.order_by('-created_at')

class ImageCreateView(generics.CreateAPIView):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageCreateSerializer

class RetrieveImageView(generics.RetrieveAPIView):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageRetrieveSerializer
    lookup_field = 'slug'


class ImageUpload(APIView):
    permission_classes = [permissions.IsAuthenticated]
