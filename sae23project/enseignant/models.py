from django.db import models

# Create your models here.
class Enseignant(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    
    prénom = models.CharField(max_length = 100)
    
    
    def __str__(self):
        chaine = f"{self.titre}␣écrit␣par␣{self.auteur}␣édité␣le␣{self.date_parution}"
        return chaine
