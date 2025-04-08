from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-created_at']
        db_table = 'test_posts'

    def __str__(self):
        return self.title
