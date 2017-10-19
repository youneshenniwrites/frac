from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    '''
    Users can post text and images to the news feed
    '''

    # each post has a unique user (creator)
    user = models.ForeignKey(User)
    # this field is not required
    title = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})
