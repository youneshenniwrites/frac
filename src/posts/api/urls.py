from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list-api'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create-api'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail-api'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update-api'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete-api'),
    url(r'^(?P<slug>[\w-]+)/like/$', LikeToggleAPIView.as_view(), name='like-api'),
]
