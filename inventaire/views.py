from django.shortcuts import render
from .models import *
import json
def home(request):
    return render(request,'inventaire/home.html')

def login(request):
    return render(request,'inventaire/login.html')


def reservations(request):

    if request.method=='POST':
   
        d=dict(request.POST)
        
        g=list(d.items())
        c=dict(g[5:])
        print(d['refReservation'][0])
        
        ref=Reservation.objects.filter(refReservation=d['refReservation'][0])[0]
      
        
        for i in range(len(c['designation'])):
            f=DetilsReservation(
                refReservation=ref,
                designation=c['designation'][i],
                qte=c['qte'][i],
                dateLivraison=c['dateLivraison'][i],
                dateRetour=c['dateRetour'][i],



            )
            
            f.save()
        
      
    
    


    return render(request,'inventaire/reservations.html')