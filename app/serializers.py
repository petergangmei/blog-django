from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user']
        read_only_fields = ['created_at', 'updated_at', 'user'] 