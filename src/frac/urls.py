from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import UserRegisterView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/profiles/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^api/posts/', include('posts.api.urls', namespace='posts-api')),
    url(r'^profiles/', include('accounts.urls', namespace='profiles')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^', include('django.contrib.auth.urls')), # Django built in login view
    url(r'^register/', UserRegisterView.as_view(), name='register'),
]
#url(r'^accounts/', include('accounts.urls'),


# serving static files in development
urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
