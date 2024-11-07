from django.db import models
from apps.companies.models import Company
from apps.categories.models import Category
from apps.languages.models import Language
from apps.images_projects.models import ImageProject

class ProjectDescription(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='descriptions')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        unique_together = ('project', 'language')  # Evita descripciones duplicadas para un proyecto y lenguaje específicos

    def __str__(self):
        return f"{self.project.title} - {self.language.name}"
    
class Project(models.Model):
    title: str = models.CharField(max_length=100)
    url:  str = models.URLField(blank=True)
    description: str = models.TextField()
    # Company is a field that connects to company information
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # Categories is a field that connects to category information
    categories = models.ManyToManyField(Category)
    # Languages is a field that connects to language information
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    # Images
    images = models.ManyToManyField(ImageProject, related_name='projects', blank=True)
    # Dates from creation and modification
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title