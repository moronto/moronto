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
    etat=models.BooleanField()
    def __str__(self):
        return self.refReservation
        
    
class DetilsReservation(models.Model):
    refReservation=models.ForeignKey(Reservation, on_delete=models.CASCADE)
    designation=models.CharField(max_length=200)
    qte=models.IntegerField()
    dateLivraison=models.DateField()
    dateRetour=models.DateField()    
    

    


