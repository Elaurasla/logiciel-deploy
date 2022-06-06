from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50,widget= forms.TextInput(attrs={'class':'form-control'}), label='Nom')
    last_name = forms.CharField(max_length=50,widget= forms.TextInput(attrs={'class':'form-control'}), label='Prénom')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')


    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur",widget= forms.TextInput(attrs={'class':'input'}))
    password= forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

