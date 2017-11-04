from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import generics

from .serializers import UsersListProfileSerializer, UserSingleProfileSerializer

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
        return get_object_or_404(User,
                                    username__iexact=self.kwargs.get('username'))
