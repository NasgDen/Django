from django.urls import path

from blogs.apps import BlogsConfig

from .views import BlogListView

app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name="blogs"),
]
