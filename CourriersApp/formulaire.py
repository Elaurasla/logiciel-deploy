from django import forms
from django.forms import ModelForm
from .models.my_model import Courrier
from .models.my_model import CourrierDepart

#from .models.my_model import CourrierDepart
from django.forms.fields import DateField , ChoiceField ,MultipleChoiceField
from django.forms.widgets import RadioSelect ,CheckboxSelectMultiple



class CourrierForm(forms.ModelForm):
    num = forms.CharField(widget=forms.NumberInput(attrs={ 'placeholder': 'Numéro'}))
    date = forms.DateField(widget=forms.TextInput(attrs={ 'placeholder': 'Date'}))
    date_emission = forms.DateField(widget=forms.TextInput(attrs={ 'placeholder': "Date d'emission"}))
    origine = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Origine'}))
    reference = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Référence'}))
    objet = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder': 'Objet'}))
    obs = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder': 'Observations'}))

    class Meta:
        model = Courrier
        fields = ['num', 'date', 'date_emission', 'reference', 'origine', 'objet','bureau','obs']

 
class CourrierDepartForm(ModelForm):
    num = forms.CharField(widget=forms.NumberInput(attrs={ 'placeholder': 'Numéro'}))
    date = forms.DateField(widget=forms.TextInput(attrs={ 'placeholder': 'Date'}))
    date_emission = forms.DateField(widget=forms.TextInput(attrs={ 'placeholder': "Date d'emission"}))
    origine = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Origine'}))
    reference = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Référence'}))
    objet = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder': 'Objet'}))
    obs = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder': 'Observations'}))

    class Meta:
        model = CourrierDepart
        fields = ['num', 'date', 'date_emission', 'reference', 'origine', 'objet','bureau','obs']
