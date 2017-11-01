from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    '''
    To be included in the posts api list and detail
    '''
    url = serializers.SerializerMethodField()
    follower_count = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse_lazy('profiles:detail', kwargs={'username': obj.username})

    def get_follower_count(self, obj):
        return 0

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'url',
            'follower_count',
        ]
