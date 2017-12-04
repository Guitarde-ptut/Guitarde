from django.db import models
from django.contrib.auth.models import User

class Tutoriel(models.Model):
    nom = models.CharField(max_length=64)
    createur = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    note = models.IntegerField                            
    description = models.CharField(max_length=500)
    video = models.CharField(max_length=100)
    def toEmbarque (self):
        return self.video.replace("watch?v=", "embed/")
        
class Commentaire(models.Model):
    auteur = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    com_tuto = models.ForeignKey('Tutoriel',
                             on_delete=models.CASCADE)
    texte = models.CharField(max_length=300)

class Note(models.Model):
    tuto = models.ForeignKey('Tutoriel',
                             on_delete=models.CASCADE,
                             related_name='note_tuto')
    utilisateur = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='note_utilisateur')
    note = models.IntegerField
    
# Create your models here.
