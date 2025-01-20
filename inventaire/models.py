from django.db import models

class Chargesaffaire(models.Model):
    
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    charge=Chargesaffaire.objects.all()
    refReservation=models.CharField(max_length=20,primary_key=True)
    chargerAffaire=models.CharField(max_length=20)
    dateReservation=models.DateField(auto_now=True)
    etat=models.BooleanField()
    def __str__(self):
        return self.id.__str__()
        
    
class DetilsReservation(models.Model):
    reservation=models.ForeignKey(Reservation, on_delete=models.CASCADE)
    designation=models.CharField(max_length=200)
    qte=models.IntegerField()
    dateLivraison=models.DateField()
    dateRetout=models.DateField()    
    def __str__(self):
        return self.reservation.__str__()

    


