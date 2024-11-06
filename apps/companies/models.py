from django.db import models

# Create your models here.
class Company(models.Model):
    name: str = models.CharField(max_length=100)
    position: str = models.CharField(max_length=100)
    image: str = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)