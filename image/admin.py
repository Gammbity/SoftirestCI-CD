from django.contrib import admin
from image.models import Image, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    readonly_fields = ['slug']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category']
    list_display_links = ['title']
    search_fields = ['title', 'user__username', 'category__name']
    list_filter = ['category', 'created_at']
    readonly_fields = ['slug']


