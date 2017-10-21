from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post

from . import serializers


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostCreateSerializer

    def perform_create(self, serializer):
        '''
        Ensures the logged in user created this post
        '''
        return serializer.save(user=self.request.user)


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetailSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostCreateSerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteAPIView(generics.DestroyAPIView):
    serializer_class = serializers.PostDetailSerializer
    lookup_field = 'slug'

    def get(self, request, slug, format=None):
        context = {'message':
                        'Proceed with the Deletion by clicking the Delete button.'}
        return Response(context)


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostListSerializer


class LikeToggleAPIView(APIView):
    def get(self, request, slug, format=None):
        post_qs = Post.objects.filter(slug=slug)
        message = 'Not allowed'
        if request.user.is_authenticated():
            liked_post = Post.objects.toggle_like(request.user, post_qs.first())
            return Response({'likes': liked_post})
        return Response({'message': message}, status=400)
