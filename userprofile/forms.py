from django import forms
from .models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        help_texts = {
            'username': None,
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
