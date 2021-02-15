from django.db import models
from client.models import Client
from produit.models import Produit

# Create your models here.

class Commande(models.Model):
    STATUS = (('en instance', 'en instance'),
              ('non livré', 'non livré'),
              ('livré', 'livré'))
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=255, choices=STATUS)
    date_creation = models.DateTimeField(auto_now_add=True)
