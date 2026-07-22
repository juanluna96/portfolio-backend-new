from django.db import models

# Create your models here.
class Language(models.Model):
    name: str = models.CharField(max_length=50)
    description: str = models.TextField()
    abbreviation: str = models.CharField(max_length=10)
    flag: str = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name