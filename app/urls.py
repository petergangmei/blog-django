from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]
