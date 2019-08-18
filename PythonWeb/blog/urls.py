from django.urls import path
from . import views

from .models import Post
from django.views.generic import DetailView, ListView

urlpatterns = [
    #path('', views.list),
    #path('', views.list, name = 'blog'),
   
    #path('', views.PostListView.as_view(), name = 'blog'),
    #path('<int:id>',views.post),
    path('', ListView.as_view(
        queryset = Post.objects.all().order_by("-date"),
        template_name = 'blog/blog.html',
        context_object_name = 'Posts',
        paginate_by = 1), name = 'blog'),
   
    #path('<int:id>',views.post, name='post'),
    #path('<int:pk>',views.PostDetailView.as_view(), name='post'),
    
    #path('<int:pk>',DetailView.as_view(
    #    model = Post,
    #    template_name = 'blog/post.html'), name='post'),
    
    path('<int:pk>',views.post, name='post'),
]