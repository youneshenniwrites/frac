from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers

from accounts.models import UserProfile
from posts.models import Post

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    '''
    To be included in the posts api list and detail
    '''
    url = serializers.SerializerMethodField()
    followed_by = serializers.SerializerMethodField()
    ifollow = serializers.SerializerMethodField()
    myPosts = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse_lazy('profiles:detail', kwargs={'username': obj.username})

    def get_followed_by(self, obj):
        return obj.followed_by.all().count()

    def get_ifollow(self, obj):
        return obj.profile.get_following().all().count()

    def get_myPosts(self, obj):
        return [post.content for post in obj.profile.get_posts()]


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'url',
            'followed_by',
            'ifollow',
            'myPosts',
        ]
