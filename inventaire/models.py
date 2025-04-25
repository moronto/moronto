from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Chargesaffaire(models.Model):
    
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    
    refReservation=models.CharField(max_length=20,primary_key=True, )
    chargerAffaire=models.CharField(max_length=20)
    dateReservation=models.DateField(default=timezone.now())
    client=models.CharField(max_length=50)
    etat=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.refReservation
        
    
class DetilsReservation(models.Model):
    refReservation=models.ForeignKey(Reservation, on_delete=models.CASCADE)
    designation=models.CharField(max_length=200)
    qte=models.IntegerField(default=1)
    dateLivraison=models.DateField(default=timezone.now())
    dateRetour=models.DateField(default=timezone.now()) 
    def __str__(self):
        return self.designation   
    



    
class Stock(models.Model):
   
    refMateriel=models.CharField(max_length=50,primary_key=True) 
    designation=models.CharField(max_length=100) 
    situation=models.CharField(max_length=50)
    lieu=models.CharField(max_length=100,null=True)
    client=models.CharField(max_length=100,null=True)
    categorie=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.refMateriel
    
class GroupeElectrogene(models.Model):
    puissance=models.CharField(max_length=50)
    marque=models.CharField(max_length=50)  
    dimension=models.CharField(max_length=50) 
    refMateriel=models.ForeignKey(Stock, on_delete=models.CASCADE)

class Modulaire(models.Model):
    gammeChoices=[
        ('evenement','EVENEMENT'),
        ('chantier','CHANTIER')
    ]
    gamme=models.CharField(max_length=50,choices=gammeChoices)  
    dimension=models.CharField(max_length=50)
    refMateriel=models.ForeignKey(Stock, on_delete=models.CASCADE)

class CabinesAutonome(models.Model):
    gammeChoices=[
        ('evenement','EVENEMENT'),
        ('chantier','CHANTIER')
    ]
    gamme=models.CharField(max_length=50,choices=gammeChoices)  
    dimension=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    refMateriel=models.ForeignKey(Stock, on_delete=models.CASCADE)

class Movement(models.Model):
    typeMovement=models.CharField(max_length=20)
    dateMovement=models.DateField()
    typeLocation=models.CharField(max_length=30)
    depot=models.CharField(max_length=30)
    refMateriel=models.CharField(max_length=30)
    designation=models.CharField(max_length=50)
    qte=models.IntegerField()
    client=models.CharField(max_length=60)
    lieu=models.CharField(max_length=60)
    matTrans=models.CharField(max_length=40,null=True)
    condTrans=models.CharField(max_length=30,null=True)
    observations=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.refMateriel

