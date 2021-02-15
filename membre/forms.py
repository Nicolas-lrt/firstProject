from django import forms
from django.forms import ModelForm

from membre.models import Membre


class ajout_form(ModelForm):
    class Meta:
        model = Membre
        fields = '__all__'




