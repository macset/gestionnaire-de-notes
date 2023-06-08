from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class ExamensForm(ModelForm):
    class Meta:
        model = models.Examens
        fields = ('titre', 'date', 'coefficient')
        labels = {
            'titre' : _('Titre'),
            'date' : _('date') ,
            'coefficient' : _('coefficient'),
        }       
