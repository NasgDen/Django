from django.urls import path

from blogs.apps import BlogsConfig

from .views import BlogListView, BlogCreateView

app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name="blogs"),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create')
]
