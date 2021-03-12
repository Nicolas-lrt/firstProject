from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Tag(models.Model):
    nom = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=255, null=True)
    prixReel = models.FloatField(null=True)
    prixBrut = models.FloatField(null=True)
    tag = models.ManyToManyField(Tag)
    smallImg = models.ImageField(upload_to='images/', null=True, blank=True)
    mainImg = models.ImageField(upload_to='images/', null=True, blank=True)
    note = models.IntegerField(null=True, default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    veryShortDesc = models.CharField(max_length=60, validators=[MinLengthValidator(32)], null=True)
    shortDesc = models.CharField(max_length=300, null=True)
    longDesc = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.nom

    def savings(self):
        return self.prixBrut-self.prixReel

    def cashBackValue(self):
        value = int((self.savings()/self.prixBrut)*100)
        return value
