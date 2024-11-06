from django.db import models

# Create your models here.
class Company(models.Model):
    name: str = models.CharField(max_length=100)
    position: str = models.CharField(max_length=100)
    image = models.ImageField(upload_to='company_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'companies'
        verbose_name = 'company'