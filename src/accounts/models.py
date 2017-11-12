from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.db.models.signals import post_save


class UserProfileManager(models.Manager):
    user_for_related_fields = True

    def all(self):
        '''
        Users won't be followed by themselves
        '''
        qs = self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs

    def toggle_follow(self, user, to_toggle_user):
        '''
        follow unfollow users
        '''
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if user_profile.following.filter(username=to_toggle_user).exists():
            user_profile.following.remove(to_toggle_user)
            added = False
        else:
            user_profile.following.add(to_toggle_user)
            added = True
        return added

    def is_following(self, user, followed_by_user):
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            return False

        if followed_by_user in user_profile.following.all():
            return True
        return False


class UserProfile(models.Model):
    '''
    Extends the Django User model
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        blank=True,
                                        related_name='followed_by')

    objects = UserProfileManager()

    def get_posts(self):
        '''
        all posts for a single user
        '''
        return self.user.post_set.all()

    def get_likes(self):
        '''
        all likes for a single user
        '''
        pass

    def get_following(self):
        '''
        Users won't be following themselves
        '''
        users = self.following.all()
        return users.exclude(username=self.user.username)

    def get_follow_url(self):
        '''
        Redirect to after toggle follow
        '''
        return reverse_lazy('profiles:follow',
                            kwargs={'username':self.user.username})

    def get_absolute_url(self):
        return reverse_lazy('profiles:detail',
                            kwargs={'username':self.user.username})

    def __str__(self):
        return 'Followers ({}); Following ({})'.format(
                                          self.user.followed_by.all().count(),
                                          self.get_following().count()
                                          )


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    '''
    Django signals to automatically create
    a user profile when a user object is created
    '''
    if created:
        new_profile, is_created = UserProfile.objects.get_or_create(user=instance)
        # make a default follower for the new user (trydjango 6:51:58)

post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)
