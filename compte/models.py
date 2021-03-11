from django.contrib.auth.models import User
from django.db import models
from produit.models import Produit


# Create your models here.


class Compte(models.Model):
    user = models.ForeignKey(User, verbose_name='Utilisateur associé', on_delete=models.CASCADE)
    userId = models.IntegerField(null=True)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username


class CartLine(models.Model):
    """
    Une ligne de panier client.
    """
    client = models.ForeignKey(Compte, on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Ligne d\'un panier client'
        verbose_name_plural = 'Lignes d\'un panier client'

    def total(self):
        return round(self.product.prix * float(self.quantity), 2)

    def __str__(self):
        return 'Ligne de panier du client \'' + self.client.user.username + '\''

