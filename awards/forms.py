from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Project,Votes

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

rating_choices = [ 
    (1, '1'), 
    (2, '2'), 
    (3, '3'), 
    (4, '4'), 
    (5, '5'), 
    (6, '6'), 
    (7, '7'), 
    (8, '8'),
    (9, '9'), 
    (10, '10'),
]  
class VotesForm(forms.Form):
    design = forms.CharField(label='Design level', widget=forms.RadioSelect(choices=rating_choices))

    usability = forms.CharField(label='Usability level', widget=forms.RadioSelect(choices=rating_choices))

    creativity  = forms.CharField(label='Creativity level', widget=forms.RadioSelect(choices=rating_choices))

    content = forms.CharField(label='Content level', widget=forms.RadioSelect(choices=rating_choices))




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