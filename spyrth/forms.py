# encoding: utf-8
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from .models import *

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        widgets = { 'email': forms.TextInput(attrs={'placeholder': 'Laissez nous votre mail', 'name': 'email1', 'type':'email'})}

class ContribForm(forms.ModelForm):
    class Meta:
        model= ContactContrib
        fields=['Nom','Email','Phone','Pays','Contrib', 'Autres']
        widgets = {'Email': forms.TextInput(attrs={'type':'email', 'placeholder':'Votre adresse mail', 'class':'input__field input__field--ichiro', 'id':'input-26'}),
                    'Phone': forms.TextInput(attrs={'placeholder':'Votre numéro de téléphone', 'class':'input__field input__field--ichiro', 'id':'input-27'}),
                    'Pays': forms.TextInput(attrs={'placeholder':'Pays', 'class':'input__field input__field--ichiro', 'id':'input-28'}),
                   'Autres': forms.Textarea(attrs={'placeholder':'Votre Message', 'name':'message'}),
                   'Nom': forms.TextInput(attrs={'placeholder':'Nom & Prénom', 'class':'input__field input__field--ichiro', 'id':'input-25'})}