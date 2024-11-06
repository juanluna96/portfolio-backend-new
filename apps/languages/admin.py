from django.contrib import admin
from .models import Language

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'abreviation', 'flag', 'created_at', 'updated_at')
    search_fields = ('name', 'abreviation')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Language, LanguageAdmin)
