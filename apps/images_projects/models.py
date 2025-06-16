from django.db import models
from main.storage_backend import media_storage

class ImageProject(models.Model):
    name = models.CharField(max_length=100, default='default_image_name') 
    image = models.ImageField(upload_to='images/projects/', storage=media_storage)
    # Date fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Images Projects'
        verbose_name = 'Image'
