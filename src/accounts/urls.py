from django.conf.urls import url
from django.urls import reverse_lazy

from .views import UserProfileView, UserFollowView


urlpatterns = [
    # user profile urls
    url(r'^(?P<username>[\w.@+-]+)/$', UserProfileView.as_view(),
                                        name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(),
                                                name='follow'),
]
