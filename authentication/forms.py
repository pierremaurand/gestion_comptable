from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms

from . import models 

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'role']
        

class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['profile_photo']