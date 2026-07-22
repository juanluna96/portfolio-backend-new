from django.db import models

from apps.areas.models import Area
from apps.languages.models import Language
from django.core.exceptions import ValidationError
from main.storage_backend import media_storage

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    color_text = models.CharField(max_length=7)
    color_bg = models.CharField(max_length=7)
    logo: str = models.CharField(max_length=255, default='', blank=True)
    image = models.ImageField(upload_to='images/categories/', storage=media_storage)
    imageBig = models.ImageField(upload_to='images/categories/', storage=media_storage)
    area_id: int = models.ForeignKey(Area, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'
        
    def __str__(self):
        return self.name
    
# Nuevo modelo para la descripción de la categoría en distintos idiomas
class CategoryDescription(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='descriptions')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category Description'
        verbose_name_plural = 'Category Descriptions'
        

    def __str__(self):
        return f"{self.category.name} - {self.language.name}"