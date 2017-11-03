'''
frac will have a list view of the users posts
and a detail view for a single post for commenting.

ListView:
user can see her own and her followers posts, and like them.
DetailView:
user can comment on a single post.
'''

from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic import (
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                    ListView,
                                    )

from .models import Post
from .forms import PostModelForm
from .mixins import OwnerPostMixin, OwnerOrAdminMixin


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_create.html'
    form_class = PostModelForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    queryset = Post.objects.all()
    template_name = 'posts/post_detail.html'


class PostUpdateView(LoginRequiredMixin, OwnerPostMixin, UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = 'posts/post_edit.html'


class PostDeleteView(LoginRequiredMixin, OwnerOrAdminMixin, DeleteView):
    queryset = Post.objects.all()
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts:list')


class PostListView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
