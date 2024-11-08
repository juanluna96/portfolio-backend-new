from django.db import models

# Create your models here.
class Biography(models.Model):
    description = models.TextField(max_length=500, blank=True)
    stacks_description = models.TextField(max_length=500, blank=True)
    about_me = models.TextField(max_length=1000, blank=True)
    phone_1 = models.CharField(max_length=15, blank=True)
    phone_2 = models.CharField(max_length=15, blank=True)
    email_1 = models.EmailField(max_length=255, unique=True)
    email_2 = models.EmailField(max_length=255, blank=True)

    def __str__(self):
        return self.email_1