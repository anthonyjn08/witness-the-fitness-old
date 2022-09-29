from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog


class BlogAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('blog_post')


admin.site.register(Blog, BlogAdmin)
