from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class RuniteForm(ModelForm):
    class Meta:
        model = models.Runite
        fields = ['nom', 'descriptif', 'coefficient']
        labels = {
            'nom': _('Nom'),
            'descriptif': _('Descriptif'),
            'coefficient': _('Coefficient'),
        }
            