from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")


# Register your models here.
admin.site.register(Article, ArticleAdmin)
