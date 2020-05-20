from django.contrib import admin
from .models import *

admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'content', 'post', 'created_date')
    list_filter = ('active', 'created_date')
    search_fields = ('owner', 'content')
    actions = ['approve_comments']
    
    
    def approve_comments(self, request,queryset):
        queryset.update(active=True)