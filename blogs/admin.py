from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'created_at', 'is_published',)
    list_filter = ('created_at',)
    search_fields = ('name', 'is_published',)
