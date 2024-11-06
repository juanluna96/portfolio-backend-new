from django.contrib import admin
from.models import Area

# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

admin.site.register(Area, AreaAdmin)
