from django.db import models
from inventaire.models import *

class Livraison(models.Model):
    bl=models.CharField(max_length=10,primary_key=True)
    client=models.CharField(max_length=60)
    dateLivraison=models.DateField()
    typeLivraison=models.CharField(max_length=30)
    chargerAffaire=models.CharField(max_length=40)
    chantier=models.CharField(max_length=50)
    created_by=models.CharField(max_length=50)
    def __str__(self):
        return str(self.bl)
    
    def generateBL(self):
        data=Livraison.objects.values_list("bl")
    
class DetailsLivraison(models.Model):
    bl=models.ForeignKey(Livraison, on_delete=models.CASCADE)
    refMateriel=models.CharField(max_length=30)
    designation=models.CharField(max_length=50)
    qte=models.IntegerField()
    matTrans=models.CharField(max_length=40,null=True)
    condTrans=models.CharField(max_length=30,null=True)
    observations=models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.bl)
    

class Mouvement(models.Model):
    typeMovement=models.CharField(max_length=20)
    dateMovement=models.DateField()
    refMateriel=models.CharField(max_length=30)
    designation=models.CharField(max_length=50)
    qte=models.IntegerField()
    matTrans=models.CharField(max_length=40,null=True)
    condTrans=models.CharField(max_length=30,null=True)
    observations=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.refMateriel





    

