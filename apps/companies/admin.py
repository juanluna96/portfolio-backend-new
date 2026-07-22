from django.contrib import admin
from.models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'image', 'created_at', 'updated_at')
    search_fields = ('name', 'position')
    list_filter = ('created_at', 'updated_at')
    

admin.site.register(Company, CompanyAdmin)