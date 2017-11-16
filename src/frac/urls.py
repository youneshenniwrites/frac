from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.contrib.auth.views import (
        LoginView,
        LogoutView,
        PasswordResetView,
        PasswordResetDoneView,
        PasswordChangeView,
        PasswordChangeDoneView,
        PasswordResetConfirmView,
        PasswordResetCompleteView
)

from accounts.views import (register, activate)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/profiles/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^api/posts/', include('posts.api.urls', namespace='posts-api')),
    url(r'^profiles/', include('accounts.urls', namespace='profiles')),
    url(r'^posts/', include('posts.urls', namespace='posts')),

    # sign up with email confirmation
    url(r'^register/', register, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),

    # Django built in login, logout, password change and reset class-based views
    url('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url('password_change/',
        PasswordChangeView.as_view(template_name='accounts/password_change.html'),
        name='password_change'),
    url('password_change/done/',
        PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'),
    url('password_reset/done/',
        PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    url('password_reset/',
        PasswordResetView.as_view(template_name='accounts/password_reset.html'),
        name='password_reset'),
    url('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url('reset/done/',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),

    # custom registration url for users
    #url(r'^register/', UserRegisterView.as_view(), name='register'),
]

# serving static and media files in development
if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
