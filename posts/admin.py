from django.contrib import admin
from .models import *

admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'content', 'post', 'created_on')
    list_filter = ('active', 'created_on')
    search_fields = ('username', 'content')
    actions = ['approve_comments']
    
    
    def approve_comments(self, request,queryset):
        queryset.update(active=True)