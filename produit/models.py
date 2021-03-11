from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Tag(models.Model):
    nom = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=255, null=True)
    prix = models.FloatField(null=True)
    tag = models.ManyToManyField(Tag)
    note = models.IntegerField(null=True, blank=True)
    veryShortDesc = models.CharField(max_length=60, validators=[MinLengthValidator(32)], null=True)
    shortDesc = models.CharField(max_length=300, null=True)
    longDesc = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.nom

