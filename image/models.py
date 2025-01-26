from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.utils.text import slugify

year = datetime.datetime.now().date().year
month = datetime.datetime.now().date().month

class Category(models.Model):
    slug = models.SlugField(max_length=300, unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):  
        return self.name
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class Image(models.Model):
    slug = models.SlugField(max_length=300, unique=True)
    img = models.ImageField(upload_to=f"images/{year}/{month}/")
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='images', default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=255)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"