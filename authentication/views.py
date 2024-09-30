from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.conf import settings

from . import forms

def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(form.cleaned_data['username'], form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/login.html', context={'form': form})


def logout_user(request):
    logout(request)
    return redirect(settings.LOGIN_URL)


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm()
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentication/upload_profile_photo.html', context={'form': form})