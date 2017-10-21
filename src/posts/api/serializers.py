from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from posts.models import Post


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
    url = post_detail_url
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    class Meta:
        model = Post
        fields = [
            'id',
            'username',
            'title',
            'slug',
            'content',
            'url',
        ]


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    username = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_date_created(self, obj):
        return obj.created.strftime('%b %d %Y | at %I:%M %p')

    def get_likes(self, obj):
        # total number of likes
        return obj.likes.all().count()

    class Meta:
        model = Post
        fields = [
            'id',
            'username',
            'title',
            'slug',
            'content',
            'url',
            'date_created',
            'likes',
        ]
