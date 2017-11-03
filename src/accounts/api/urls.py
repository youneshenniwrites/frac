from django.conf.urls import url

from .views import UserListAPIVIew, UserDetailAPIVIew


urlpatterns = [
    url(r'^$', UserListAPIVIew.as_view(), name='users-list-api'),
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailAPIVIew.as_view(), name='user-posts-api'),
]
