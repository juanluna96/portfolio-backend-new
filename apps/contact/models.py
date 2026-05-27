from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100, blank=True, default='')
    country_code = models.CharField(max_length=10, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    address = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    read = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)