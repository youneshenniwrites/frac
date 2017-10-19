from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView

from .forms import UserRegisterForm

User = get_user_model()

class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'accounts/user_registration.html'
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
        new_user.set_password(password)
        new_user.save()

        return super(UserRegisterView, self).form_valid(form)
