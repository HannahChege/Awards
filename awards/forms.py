from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Project

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['project_name', 'pub_date','profile','user']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
    }
class ProfileForm(forms.ModelForm):

    class Meta:
        model =Profile
        exclude=['user']
  

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['username']