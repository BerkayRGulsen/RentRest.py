from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import FileInput
from django.utils.translation import gettext_lazy as _

from Reservations.models import Visitor


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'
        exclude = ['user', 'role']

        labels = {
            'username': _('Usename:'),
            'first_name': _('Name:'),
            'last_name': _('Surname:'),
            'profile_pic': _('Profile image:'),
        }

        widgets = {
            'profile_pic': FileInput(),
        }
