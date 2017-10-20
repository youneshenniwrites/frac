from django.conf.urls import url

from .views import (PostCreateView,
                    PostDetailView,
                    PostListView,
                    PostDeleteView,
                    PostUpdateView)


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteView.as_view(), name='delete'),
]
