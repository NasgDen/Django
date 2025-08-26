from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Blog


class BlogListView(ListView):
    """ Класс реализующий интерфейс для отображения блогов """

    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogCreateView(CreateView):
    """ Класс реализующий интерфейс для создания блога """

    model = Blog
    fields = ['name', 'content', 'image', 'is_published']
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy("blogs:blogs")


class BlogDetailView(DetailView):
    """ Класс реализующий интерфейс для детального просмотра блога """

    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """ Класс реализующий интерфейс для редактирования блога """

    model = Blog
    fields = ['name', 'content', 'image', 'is_published']
    template_name = 'blog/blog_create.html'

    def get_success_url(self):
        return reverse_lazy("blogs:blog_detail", kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    """ Класс реализующий интерфейс для удаления блога """

    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy("blogs:blogs")
