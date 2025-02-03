from django.db import models

class Chargesaffaire(models.Model):
    
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    
    refReservation=models.CharField(max_length=20,primary_key=True,)
    chargerAffaire=models.CharField(max_length=20)
    dateReservation=models.DateField(auto_now=True)
    client=models.CharField(max_length=50)
    etat=models.CharField(max_length=20)
    def __str__(self):
        return self.refReservation
        
    
class DetilsReservation(models.Model):
    refReservation=models.ForeignKey(Reservation, on_delete=models.CASCADE)
    designation=models.CharField(max_length=200)
    qte=models.IntegerField(default=1)
    dateLivraison=models.DateField(auto_now_add=True)
    dateRetour=models.DateField() 
    def __str__(self):
        return self.designation   
    



    
class Stock(models.Model):
    # etat=[("louer","LOUER"),
    #       ("disponible","DISPONIBLE"),
    #       ("vente","VENTE"),
    #       ("don","DON"),
    #       ("verifie","A VERIFIER"),
    #       ("utiliser","UTILISER"),
    #       ]
    # cat=[("GROUPE ELECTROGENE","GROUPE ELECTROGENE"),
    #       ("MOUDULAIRE","MOUDULAIRE"),
    #       ("CABINE AUTONOME","CABINE AUTONOME"),
    #       ]
    refMateriel=models.CharField(max_length=50,primary_key=True) 
    designation=models.CharField(max_length=100) 
    situation=models.CharField(max_length=50)
    lieu=models.CharField(max_length=100)
    categorie=models.CharField(max_length=50)

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


