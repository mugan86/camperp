from django.contrib import admin
from .models import Post, PostType, PostCategory


class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'description', 'created_date', )

admin.site.register(Post)
admin.site.register(PostType, PostTypeAdmin)
admin.site.register(PostCategory)