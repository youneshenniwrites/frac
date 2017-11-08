from django.conf.urls import url

from .views import (UserListAPIVIew, UserDetailAPIVIew , FollowToggleAPIView)


urlpatterns = [
    url(r'^$', UserListAPIVIew.as_view(), name='users-list-api'),
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailAPIVIew.as_view(), name='user-posts-api'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', FollowToggleAPIView.as_view(), name='follow-api'),
]
