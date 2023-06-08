from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class UniteForm(ModelForm):
    class Meta:
        model = models.Unite
        fields = ['Nom', 'semestre', 'crédit_ECTS']
        labels = {
            'Nom': _('Nom'),
            'semestre': _('semestre'),
            'crédit_ECTS': _('crédit ECTS'),

        }
            