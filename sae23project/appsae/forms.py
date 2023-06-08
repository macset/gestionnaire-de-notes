from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class EtudiantForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = ('nom', 'prénom', 'groupe', 'photo','email')
        labels = {
            'nom' : _('Titre'),
            'prénom' : _('prénom') ,
            'groupe' : _('groupe'),
            'photo' : _('photo'),
            'email' : _('email')
        }       
