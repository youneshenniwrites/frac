from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls', namespace='posts')),
]
#url(r'^accounts/', include('accounts.urls'),


# serving static files in development
urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
