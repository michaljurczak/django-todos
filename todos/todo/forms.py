from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'row center-item'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'row center-item'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    class Meta:
        model = User
        fields = ['username', 'email' ,'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'row center-item', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'row center-item', 'placeholder': 'e-mail', 'required': True}),
        }
