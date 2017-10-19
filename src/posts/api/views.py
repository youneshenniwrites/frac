from rest_framework import generics
from rest_framework.response import Response

from posts.models import Post

from . import serializers


class PostCreateAPIView(generics.CreateAPIView):
    model = Post
    serializer_class = serializers.PostCreateSerializer

    def perform_create(self, serializer):
        '''
        Ensures the logged in user created this post
        '''
        return serializer.save(user=self.request.user)


class PostDetailAPIView(generics.RetrieveAPIView):
    model = Post
    serializer_class = serializers.PostDetailSerializer
    try:
        lookup_field = 'slug'
    except:
        pass


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostListSerializer


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.PostCreateSerializer


class PostDeleteAPIView(generics.DestroyAPIView):
    serializer_class = serializers.PostCreateSerializer
