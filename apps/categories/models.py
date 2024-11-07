from django.db import models

from apps.areas.models import Area
from apps.languages.models import Language
from django.core.exceptions import ValidationError

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    color_text = models.CharField(max_length=7)
    color_bg = models.CharField(max_length=7)
    logo: str = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/')
    imageBig = models.ImageField(upload_to='category_images/')
    area_id: int = models.ForeignKey(Area, on_delete=models.CASCADE)
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
        unique_together = ('category', 'language')
        verbose_name = 'Category Description'
        verbose_name_plural = 'Category Descriptions'
        
    def clean(self):
        if CategoryDescription.objects.filter(category=self.category, language=self.language).exists():
            raise ValidationError("This category already has a description in this language.")

    def __str__(self):
        return f"{self.category.name} - {self.language.name}"