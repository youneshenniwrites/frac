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
        return sum([post.likes.count() for post in obj.post_set.all()])


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'all_myLikes',
            'all_myFollowers',
            'iFollow',
            'all_myPosts',
            'profileApiURL',
        ]


class UserSingleProfileSerializer(UsersListProfileSerializer):
    all_myPosts_content = serializers.SerializerMethodField()
    all_myFollowers_list = serializers.SerializerMethodField()
    iFollow_list = serializers.SerializerMethodField()
    followed_boolean = serializers.SerializerMethodField()
    loggedIn = serializers.SerializerMethodField()

    def get_all_myPosts_content(self, obj):
        '''
        displays a list of all my posts
        '''
        return [post.content for post in obj.profile.get_posts()]

    def get_all_myFollowers_list(self, obj):
        '''
        displays a list of all my followers
        '''
        return [follower.user.username for follower in obj.followed_by.all()]

    def get_iFollow_list(self, obj):
        return [ifollow.username for ifollow in obj.profile.get_following().all()]

    def get_followed_boolean(self, obj):
        if "followed" in self.context:
            return self.context["followed"]
        return 'error'

    def get_loggedIn(self, obj):
        if "loggedIn" in self.context:
            return self.context["loggedIn"]
        return 'error'


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
            'all_myFollowers_list',
            'iFollow_list',
            'followed_boolean',
            'loggedIn'
        ]
