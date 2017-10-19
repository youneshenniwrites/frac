from django.conf.urls import url

from .views import (PostCreateView, PostDetailView, PostListView)


urlpatterns = [
    url(r'^(?P<pk>\d+)$', PostDetailView.as_view(), name='detail'),
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^$', PostListView.as_view(), name='list'),

]
