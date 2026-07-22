from django.contrib import admin
from .models import Language

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'abbreviation', 'flag', 'created_at', 'updated_at')
    search_fields = ('name', 'abbreviation')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Language, LanguageAdmin)
