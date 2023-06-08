from django.db import models

# Create your models here.
class Unite(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    Nom = models.CharField(max_length=50) # défini un champs de type texte de 100 caractères maximum
    
    semestre = models.IntegerField(max_length = 1)
    
    crédit_ECTS = models.IntegerField(blank=True, max_length= 3)
    def __str__(self):
        chaine = f"{self.titre}␣écrit␣par␣{self.auteur}␣édité␣le␣{self.date_parution}"
        return chaine