from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class ExamensForm(ModelForm):
    class Meta:
        model = models.Examens
        fields = ('id','titre', 'date', 'coefficient')
        labels = {
            'id' :_('id'),
            'titre' : _('Titre'),
            'date' : _('date') ,
            'coefficient' : _('coefficient'),
        }    


class EtudiantForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = ('Netudiant','nom', 'prénom', 'groupe', 'photo', 'email')
        labels = {
            'Netudiant' :_('Netudiant'),
            'nom': _('Nom'),
            'prénom': _('Prénom'),
            'groupe': _('Groupe'),
            'photo': _('Photo'),
            'email': _('Email')
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class EnseignantForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = ('id','nom', 'prénom')
        labels = {
            'id' :_('id'),
            'nom' : _('nom'),
            'prénom' : _('prénom'),
        }       
        

 
class RuniteForm(ModelForm):
    class Meta:
        model = models.Runite
        fields = ['code_ressource','Nom', 'descriptif', 'coefficient']
        labels = {
            'code_ressource' :_('code ressource'),
            'Nom': _('Nom'),
            'descriptif': _('Descriptif'),
            'coefficient': _('Coefficient'),
        }
        
        
        
class UniteForm(ModelForm):
    class Meta:
        model = models.Unite
        fields = ['code','Nom', 'semestre', 'crédit_ECTS']
        labels = {
            'code' :_('code'),
            'Nom': _('Nom'),
            'semestre': _('semestre'),
            'crédit_ECTS': _('crédit ECTS'),

        }
            


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
