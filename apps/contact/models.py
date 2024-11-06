from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    message = models.TextField()
    read = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)