from django.conf.urls import url

from .views import UserProfileView, UserFollowView


urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserProfileView.as_view(), name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),
]
