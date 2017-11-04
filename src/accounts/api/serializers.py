from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

from accounts.models import UserProfile
from posts.models import Post

User = get_user_model()

profile_detail_url = HyperlinkedIdentityField(
        view_name='profiles-api:user-posts-api',
        lookup_field='username'
        )


class UsersListProfileSerializer(serializers.ModelSerializer):
    '''
    To be included in the posts api list and detail
    '''
    all_myFollowers = serializers.SerializerMethodField()
    iFollow = serializers.SerializerMethodField()
    all_myPosts = serializers.SerializerMethodField()
    all_myLikes = serializers.SerializerMethodField()
    profileApiURL = profile_detail_url

    def get_all_myFollowers(self, obj):
        return obj.followed_by.all().count()

    def get_iFollow(self, obj):
        return obj.profile.get_following().all().count()

    def get_all_myPosts(self, obj):
        '''
        counts all posts for a user
        '''
        return obj.post_set.all().count()

    def get_all_myLikes(self, obj): # obj = person.user in the shell
        '''
        counts all likes for a user
        '''
        list_all_likes = []
        for post in obj.post_set.all():
            list_all_likes.append(post.likes.count())
        return sum(list_all_likes)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'all_myLikes',
            'all_myFollowers',
            'iFollow',
            'all_myPosts',
            'profileApiURL',
        ]


class UserSingleProfileSerializer(UsersListProfileSerializer):
    all_myPosts_content = serializers.SerializerMethodField()

    def get_all_myPosts_content(self, obj):
        '''
        displays all posts for a user
        '''
        return [post.content for post in obj.profile.get_posts()]

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'all_myPosts',
            'all_myLikes',
            'all_myFollowers',
            'iFollow',
            'all_myPosts_content',
        ]
