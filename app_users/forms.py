from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    city = forms.CharField(max_length=30)
    photo_profile = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('photo_profile', 'username', 'first_name', 'last_name', 'email', 'city', 'password1', 'password2')


class EditUserForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image')
