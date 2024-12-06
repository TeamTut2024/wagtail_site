from django.apps import AppConfig


class BlogPostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wagtail_site.blog_post'
    verbose_name = 'Blog Post'
