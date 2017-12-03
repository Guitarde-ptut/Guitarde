from django.db import models

class Tutoriel(models.Model):
    nom = models.CharField(max_length=64)
    createur = models.ForeignKey('Utilisateur',
                                 on_delete=models.CASCADE)
    note = models.IntegerField                            
    description = models.CharField(max_length=500)
    video = models.CharField(max_length=100)

class Utilisateur(models.Model):
    courriel = models.CharField(max_length=64)
    nom = models.CharField(max_length=16)
    mdp = models.CharField(max_length=64)

class Commentaire(models.Model):
    auteur = models.ForeignKey('Utilisateur',
                               on_delete=models.CASCADE)
    com_tuto = models.ForeignKey('Tutoriel',
                             on_delete=models.CASCADE)
    texte = models.CharField(max_length=300)

class Note(models.Model):
    tuto = models.ForeignKey('Tutoriel',
                             on_delete=models.CASCADE,
                             related_name='note_tuto')
    utilisateur = models.ForeignKey('Tutoriel',
                                    on_delete=models.CASCADE,
                                    related_name='note_utilisateur')
    note = models.IntegerField
    
# Create your models here.
