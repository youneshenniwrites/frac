from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, View
from django.views.generic.edit import FormView

from .models import UserProfile
from .forms import UserRegisterForm

User = get_user_model()

class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'registration/user_registration.html'
    success_url = '/login'

    def form_valid(self, form):
        '''
        Override the form_valid method to
        check for valid fields and hashing the password
        before saving the new user to the database.
        '''
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create(username=username, email=email)
        # hashes the password 
        new_user.set_password(password)
        new_user.save()

        return super(UserRegisterView, self).form_valid(form)


class UserProfileView(DetailView):
    template_name = 'accounts/user_profile.html'
    queryset = User.objects.all()

    def get_object(self):
        '''
        lookup field with username for the url
        '''
        return get_object_or_404(User,
                                    username__iexact=self.kwargs.get('username'))

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(self.request.user, self.get_object())
        context['following'] = following
        return context


class UserFollowView(View):
    '''
    follow toggle based on a url
    '''
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect("profiles:detail", username=username)
