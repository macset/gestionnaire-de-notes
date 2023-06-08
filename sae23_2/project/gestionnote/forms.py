from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class ExamensForm(ModelForm):
    class Meta:
        model = models.Examens
        fields = ('titre', 'date', 'coefficient')
        labels = {
            'titre' : _('Titre'),
            'date' : _('date') ,
            'coefficient' : _('coefficient'),
        }    


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
