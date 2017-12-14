"""
Counter class takes a list of items and outputs a dictionary
with number of occurence (value) of each item (keys) in the list
"""
from collections import Counter

from itertools import chain # returns multiple items in a list comprehension

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

from accounts.models import UserProfile
from posts.models import Post

from .gifts import reverse

User = get_user_model()

profile_detail_url = HyperlinkedIdentityField(
        view_name='profiles-api:user-posts-api',
        lookup_field='username'
        )

gift_for_likes =   {
                    2: 'Stamp', 4: 'Mug', 8: 'Sunglasses', 16: 'Jacket',
                    32: 'Hat', 64: 'Shoes', 128: 'Bag', 256: 'Sliver Ring',
                    512: 'Gold Ring', 1024: 'Tesla', 2048: 'Jet'
                    }

likes_for_gift = reverse(gift_for_likes)


class UsersListProfileSerializer(serializers.ModelSerializer):
    '''
    To be included in the posts api list and detail
    '''
    all_myFollowers = serializers.SerializerMethodField()
    iFollow         = serializers.SerializerMethodField()
    all_myPosts     = serializers.SerializerMethodField()
    all_myLikes     = serializers.SerializerMethodField()
    profileApiURL   = profile_detail_url

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
    all_myPosts_content     = serializers.SerializerMethodField()
    all_myFollowers_list    = serializers.SerializerMethodField()
    iFollow_list            = serializers.SerializerMethodField()
    followed_boolean        = serializers.SerializerMethodField()
    loggedIn                = serializers.SerializerMethodField()
    list_of_gifts           = serializers.SerializerMethodField()

    def get_all_myPosts_content(self, obj):
        '''
        displays a list of all my posts
        '''
        return chain.from_iterable((
                                    f'Post ID: {post.id}',
                                    f'Post title: {post.title}',
                                    f'Post content: {post.content}',
                                    f'Post likes: {post.likes.all().count()}'
                                    )
                                    for post in obj.profile.get_posts())

    def get_all_myFollowers_list(self, obj):
        '''
        displays a list of all my followers
        '''
        if obj.followed_by.all().count() == 0:
            return 'You have no followers yet.'
        return [follower.user.username for follower in obj.followed_by.all()]

    def get_iFollow_list(self, obj):
        if obj.profile.get_following().all().count() == 0:
            return 'You are not following anyone yet.'
        return [ifollow.username for ifollow in obj.profile.get_following().all()]

    def get_followed_boolean(self, obj):
        if "followed" in self.context:
            return self.context["followed"]
        return 'error'

    def get_loggedIn(self, obj):
        if "loggedIn" in self.context:
            return self.context["loggedIn"]
        return 'error'

    def get_list_of_gifts(self, obj):
        '''
        Checks the likes for each post against the keys of gift dict.
        Returns the gift for likes and the latest biggest gift group
        '''
        matches = []
        numLikes = []
        final_matches = []
        posts_likes = []

        for post in obj.profile.get_posts():
            numLikes.append(post.likes.all().count())
        # logic for gift per post
        if len(numLikes) != 0:
            for like in numLikes:
                for key in gift_for_likes.keys():
                    if like >= key:
                        matches.append(key)
                        final_matches.append(gift_for_likes.get(matches[-1]))
        # get the latest gift series
        for i in final_matches:
            posts_likes.append(likes_for_gift.get(i))
            latest_gift_series = gift_for_likes.get(max(posts_likes))
            gifts_and_numbers = Counter(final_matches)

        return (gifts_and_numbers,
                final_matches,
                str(posts_likes.count(max(posts_likes))) + " " + latest_gift_series
                )

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
            'loggedIn',
            'list_of_gifts'
        ]
