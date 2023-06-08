from django.db import models

# Create your models here.
class Note(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    examens = models.CharField(max_length=50) # défini un champs de type texte de 100 caractères maximum
    
    etudiant = models.CharField(max_length = 50)
    
    note = models.IntegerField(blank=False, max_length = 4) # champs de type date, pouvant être null ou ne pas être rempli
    
    appréciation = models.CharField(blank=True, max_length=1000) # champs de type entier devant être obligatoirement rempli
    
    def __str__(self):
        chaine = f"{self.titre}␣écrit␣par␣{self.auteur}␣édité␣le␣{self.date_parution}"
        return chaine
