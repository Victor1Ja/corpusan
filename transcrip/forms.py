from django import forms
from .models import Transcrip
from django.utils.translation import gettext_lazy as _

class TranscripForm(forms.ModelForm):
    class Meta:
        model = Transcrip
        fields = '__all__'
        labels = {
            'code': 'Código',
            'city': 'Ciudad',
            'country': 'País',
            'descrip': 'Ficha Técnica',
            'transcrip': 'Transcripción',
            'audio':'Grabación'
        }
