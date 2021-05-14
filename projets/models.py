from django.db import models

# Create your models here.


class Projet(models.Model):
    nom = models.CharField(max_length=255)
    dateBesoin = models.DateField(auto_now=False, null=True)
    description = models.TextField(max_length=3000, null=True)
    nbMembre = models.IntegerField(null=True)
    analyse = models.TextField(max_length=3000, null=True)
    etape_de_developpement = models.TextField(max_length=3000, null=True)
    strategie_de_sortie = models.TextField(max_length=3000, null=True)
    usage_des_fonds = models.TextField(max_length=3000, null=True)
    prenom_contact = models.CharField(max_length=255, null=True)
    nom_contact = models.CharField(max_length=255, null=True)
    mail_contact = models.EmailField(max_length=255, null=True)
    tel_contact = models.CharField(max_length=255, null=True)
    siret_societe = models.CharField(max_length=255, null=True)
    fonction_contact = models.CharField(max_length=255, null=True)
    societe_doc = models.FileField(upload_to='project-files/', null=True, blank=True)
    bilan_doc = models.FileField(upload_to='project-files/', null=True, blank=True)
    ex_projet_reussi_doc = models.FileField(upload_to='project-files/', null=True, blank=True)
    desc_operation_doc = models.FileField(upload_to='project-files/', null=True, blank=True)
    news = models.TextField(max_length=3000, null=True)
    questions = models.TextField(max_length=3000, null=True)
    temoignage = models.TextField(max_length=3000, null=True)
