from django.db import models

# Create your models here.

class Area(models.Model):
    title = models.CharField(max_length=100)
    name = models.TextField()
    logo: str = models.CharField(max_length=255)
    ad_id = models.CharField(max_length=20, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)