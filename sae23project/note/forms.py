from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class NoteForm(ModelForm):
    class Meta:
        model = models.Note
        fields = ('examens', 'etudiant', 'note', 'appréciation')
        labels = {
            'examens' : _('Examens'),
            'etudiant' : _('Etudiant'),
            'note' : _('Note'),
            'appréciation' : _('appréciation'),
        }       
