from django.db import models

from apps.areas.models import Area

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    color_text = models.CharField(max_length=7)
    color_bg = models.CharField(max_length=7)
    logo: str = models.CharField(max_length=255)
    image: str = models.CharField(max_length=255)
    imageBig: str = models.CharField(max_length=255)
    area_id: int = models.ForeignKey(Area, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)