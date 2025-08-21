from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog


class BlogListView(ListView):
    """ Класс реализующий интерфейс для отображения блогов """

    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'


class BlogCreateView(CreateView):
    """ Класс реализующий интерфейс для создания блога """

    model = Blog
    fields = ['name', 'content', 'image', 'is_published', 'count_views']
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy("blogs:blogs")


class BlogDetailView(DetailView):

    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
