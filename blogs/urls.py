from django.urls import path

from blogs.apps import BlogsConfig

from .views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView

app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name="blogs"),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name="blog_update"),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name="blog_delete"),
]
