from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'city', 'state', 'is_published', 'list_date')
    list_filter = ('is_published', 'city', 'state')
    search_fields = ('title', 'description', 'city', 'state')
