"""from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models
from CourriersApp.models.my_model import Courrier
from django.forms.fields import MultipleChoiceField

class CourrierForm(forms.ModelForm):
    OPTIONS = (
           ("finance"), ("brh"), ("contentieux"), ("logistique"), ("magasin"),("immo"),("traitements")
            )
        bureau = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = models.my_model.Courrier
        fields = ['num', 'date', 'date_emission', 'reference', 'origine', 'objet','bureau']"""
 