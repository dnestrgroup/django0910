from django.apps import AppConfig


class MyBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_blog'
    # Application name in admin panel
    verbose_name = 'Мой блог'
