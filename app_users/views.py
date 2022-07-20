from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from app_users.forms import RegisterForm, EditUserForm
from app_users.models import ProfileModel
from django.contrib.auth.models import User


class MainView(View):
    def get(self, request):
        return render(request=request, template_name='main.html')

class AuthLoginView(LoginView):
    template_name = 'login.html'

class AuthLogoutView(LogoutView):
    next_page = '/'

class RegisterView(View):
    def get(self, request):
        reg_form = RegisterForm()
        return render(request=request, template_name='register.html', context={'reg_form': reg_form})

    def post(self, request):
        reg_form = RegisterForm(request.POST, request.FILES)

        if reg_form.is_valid():

            user = reg_form.save()
            city = reg_form.cleaned_data.get('city')
            photo_profile = reg_form.cleaned_data.get('photo_profile')
            ProfileModel.objects.create(user=user, city=city, photo_profile=photo_profile)

            username = reg_form.cleaned_data.get('username')
            password = reg_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/')
        return render(request=request, template_name='register.html', context={'reg_form': reg_form})

class ProfileUserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            profile = ProfileModel.objects.get(user_id=request.user.id)
            return render(request=request, template_name='profile.html', context={'user': user, 'profile':profile})
        else:
            return HttpResponse('Вы не авторизованы, этот раздел вам недоступен. Пожалуйста, войдите в свою учётную запись.')

class EditProfileView(View):
    def get(self, request, user_id):
        if request.user.is_authenticated:
            user = User.objects.get(id=user_id)
            edit_form = EditUserForm(instance=user)
            return render(request=request, template_name='edit.html', context={'edit_form': edit_form})
        else:
            raise PermissionDenied

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        edit_form = EditUserForm(request.POST, request.FILES, instance=user)

        if edit_form.is_valid():
            edit_form.save()

            update_photo_profile = edit_form.cleaned_data.get("image")
            profile = ProfileModel.objects.get(user=user)
            profile.photo_profile = update_photo_profile
            profile.save()
            return redirect('/profile/')
        return render(request=request, template_name='blog/edit.html', context={'edit_form': edit_form, 'user_id': user_id})