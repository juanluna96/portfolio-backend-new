from django.contrib import admin
from .models import ImageProject

# Register your models here.
class ImageProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    

admin.site.register(ImageProject, ImageProjectAdmin)