'''
Users must register an account to start using this app.
'''

from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(label='Confirm Password',
                                        widget=forms.PasswordInput)

    def clean_password_again(self):
        '''
        we must ensure that both passwords are identical
        '''

        password = self.cleaned_data.get('password')
        password_again = self.cleaned_data.get('password_again')
        if password != password_again:
            raise forms.ValidationError('Passwords must match')
        return password_again

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email
