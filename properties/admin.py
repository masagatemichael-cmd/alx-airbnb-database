from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'host', 'location', 'price_per_night', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'location']