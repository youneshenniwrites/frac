from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

from .utils import unique_slug_generator


User = settings.AUTH_USER_MODEL


class PostManager(models.Manager):
    '''
    Custom Manager Functionalities
    '''

    def toggle_like(self, user, post_obj):
        '''
        User can like or dislike a post
        '''

        if user in post_obj.likes.all():
            post_liked = False
            post_obj.likes.remove(user)
        else:
            post_liked = True
            post_obj.likes.add(user)
        return post_liked


class Post(models.Model):
    '''
    Users can post text and images to the news feed
    '''

    # each post has a unique user (creator)
    user = models.ForeignKey(User)
    # this field is not required
    title = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True, related_name='liked')

    objects = PostManager()

    def __str__(self):
        #return str(self.user.username)
        return str(self.content)

    def get_absolute_url(self):
        if self.slug:
            return reverse('posts:detail', kwargs={'slug': self.slug})
        else:
            return reverse('posts:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('-created',)



def new_post_unique_slug_signal(sender, instance, *args, **kwargs):
    '''
    Django pre-save signal to set the unique slug
    for the post instance
    prior to saving it to the database
    '''

    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(new_post_unique_slug_signal, sender=Post)
