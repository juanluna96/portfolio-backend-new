from django.db import models
from main.storage_backend import media_storage

# Create your models here.
class Company(models.Model):
    name: str = models.CharField(max_length=100)
    position: str = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/companies/', storage=media_storage)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'companies'
        verbose_name = 'company'