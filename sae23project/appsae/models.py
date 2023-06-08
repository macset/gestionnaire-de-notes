from django.db import models

# Create your models here.
#des étudiants (N°étudiant, nom, prénom, groupe, photo, email),
#des Unités d'enseignement : UE (code, Nom, semestre, crédit ECTS),
#des ressources associés à une UE (code ressource, nom, descriptif, coefficient),
#des enseignants  (id, nom, prénom),
#des examens (id, titre, date, coefficient),
#des notes (examen, étudiant, note, appréciation)

from django.db import models
class Etudiant(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    
    prénom = models.CharField(max_length = 100)
    
    groupe = models.CharField(max_length = 5) # champs de type entier devant être obligatoirement rempli
    
    photo = models.ImageField(blank=True)
    
    email = models.EmailField(blank=False)
    #date_parution = models.DateField(blank=True, null = True) # champs de type date, pouvant être null ou ne pas être rempli
    #nombre_pages = models.IntegerField(blank=False) # champs de type entier devant être obligatoirement rempli
    #resume = models.TextField(null = True, blank = True) # champs de type text long
    def __str__(self):
        chaine = f"{self.nom}␣écrit␣par␣{self.prénom}␣édité␣le␣{self.email}"
        return chaine