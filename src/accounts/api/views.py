from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (UsersListProfileSerializer,
                            UserSingleProfileSerializer)

from accounts.models import UserProfile

User = get_user_model()


class UserListAPIVIew(generics.ListAPIView):
    '''
    Displays a list of users
    '''
    serializer_class = UsersListProfileSerializer

    def get_queryset(self):
        return User.objects.all()


class UserDetailAPIVIew(generics.RetrieveAPIView):
    '''
    Displays a list of a user's posts
    '''
    serializer_class = UserSingleProfileSerializer
    queryset = User.objects.all()

    def get_object(self):
        self.object = get_object_or_404(User,
                                 username__iexact=self.kwargs.get('username')
                                 )
        return self.object

    def get_serializer_context(self):
        '''
        passing the extra is_following argument to the UserDetailAPIVIew
        '''
        context = super(UserDetailAPIVIew, self).get_serializer_context()
        is_followed = self.request.user.profile.following.filter(username=self.object).exists()
        context.update({'followed': is_followed})
        print(is_followed)
        return context


class FollowToggleAPIView(APIView):
    '''
    Uses the custom model manager for user toggle follow
    '''
    def get(self, request, username, format=None):
        user_to_toggle = get_object_or_404(User, username__iexact=username)
        me = request.user
        message = 'Not allowed'

        if request.user.is_authenticated():
            # arguments as defined in the custom model manager
            is_followed = UserProfile.objects.toggle_follow(me, user_to_toggle)
            return Response({'followed': is_followed})
        return Response({'message': message}, status=400)
