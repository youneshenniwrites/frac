from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from posts.models import Post
from accounts.api.serializers import UserProfileSerializer


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]


post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail-api',
        lookup_field='slug'
        )


class PostDetailSerializer(ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    url = post_detail_url

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
            'url',
        ]


class PostListSerializer(ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    url = post_detail_url
    date_created = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    badges = serializers.SerializerMethodField()

    def get_date_created(self, obj):
        return obj.created.strftime('%b %d %Y | at %I:%M %p')

    def get_likes(self, obj):
        # total number of likes
        return obj.likes.all().count()

    def get_badges(self, obj):
        numLikes = obj.likes.all().count()
        if numLikes == 3:
            return str(numLikes) + 'Pawn'

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
            'url',
            'date_created',
            'likes',
            'badges',
        ]
