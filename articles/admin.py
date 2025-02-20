from django.contrib import admin # type: ignore

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'timestamp', 'updated']
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
