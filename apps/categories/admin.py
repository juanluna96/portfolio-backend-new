from django.contrib import admin
from.models import Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name', 'get_related_projects')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    
    def get_related_projects(self, obj):
        related_projects = obj.project_set.all()
        return ", ".join([project.title for project in related_projects])
    
    get_related_projects.short_description = 'Proyectos relacionados'

admin.site.register(Category, CategoryAdmin)