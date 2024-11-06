from django.db import models

# Create your models here.
class Project(models.Model):
    title: str = models.CharField(max_length=100)
    url:  str = models.URLField(blank=True)
    description: str = models.TextField()
    # Company is a field that connects to company information
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    # Categories is a field that connects to category information
    categories = models.ManyToManyField('categories.Category')
    # Languages is a field that connects to language information
    languages = models.ManyToManyField('languages.Language')
    # Dates from creation and modification
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    