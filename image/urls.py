from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ImageCreateView.as_view(), name='create'),
    path('list/', views.ImageListView.as_view(), name='list'),
    path('retrieve/<str:slug>/', views.RetrieveImageView.as_view(), name='retrieve'),
    path('upload/<str:slug>/', views.ImageUpload.as_view(), name='upload'),
]