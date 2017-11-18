from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from posts.models import Post
from accounts.api.serializers import UsersListProfileSerializer


post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail-api',
        lookup_field='slug'
        )


class PostListSerializer(ModelSerializer):
    user = UsersListProfileSerializer(read_only=True)
    postApiURL= post_detail_url
    date_created = serializers.SerializerMethodField()
    all_likes_post = serializers.SerializerMethodField()

    def get_date_created(self, obj):
        return obj.created.strftime('%b %d %Y | at %I:%M %p')

    def get_all_likes_post(self, obj):
        '''
        counts the total number of likes per post
        '''
        return obj.likes.all().count()

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
            'postApiURL',
            'all_likes_post',
            'date_created',
        ]


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]


class PostDetailSerializer(PostListSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
            'all_likes_post',
            'date_created',
        ]
