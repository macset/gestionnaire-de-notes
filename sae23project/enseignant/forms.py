from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class EnseignantForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = ('nom', 'prénom')
        labels = {
            'nom' : _('Titre'),
            'prénom' : _('prénom'),
        }       
