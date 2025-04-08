from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

def home(request):
    return render(request, 'home.html')

class PostListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating and deleting a post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
