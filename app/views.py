from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

def home(request):
    return render(request, 'home.html')

class PostListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating posts.
    GET: Public access - List all posts
    POST: Authenticated users only - Create a new post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        """
        GET requests are public
        POST requests require authentication
        """
        if self.request.method == 'GET':
            return []
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating and deleting a post.
    GET: Public access - Retrieve a post
    PUT/PATCH/DELETE: Authenticated users only - Update or delete a post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        """
        GET requests are public
        PUT, PATCH, DELETE requests require authentication
        """
        if self.request.method == 'GET':
            return []
        return [permissions.IsAuthenticated()]
