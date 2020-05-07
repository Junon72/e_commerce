from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=20, default="DOW Author")
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    username = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        related_name='comments',
        null=False,
		default=1
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.username)