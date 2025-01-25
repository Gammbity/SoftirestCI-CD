from django.db import models
from ckeditor.fields import RichTextField
import datetime

year = datetime.datetime.now().date().year
month = datetime.datetime.now().date().month

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):  
        return self.name
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class Image(models.Model):
    img = models.ImageField(upload_to=f"images/{year}/{month}/")
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='images', default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"