from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'content',
        ]


class PostListSerializer(ModelSerializer):
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
        ]


class PostDeleteSerializer(ModelSerializer):
    pass
