from django.db import models

# Create your models here.

class Membre(models.Model):
    ROLE = (('Entreprise', 'Entreprise'),
            ('Investisseur', 'Investisseur'),
            ('Posteur de Projet', 'Posteur de Projet'),
            ('Auto-entrepreneur', 'Auto-entrepreneur'))
    nom = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pswd = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=ROLE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom