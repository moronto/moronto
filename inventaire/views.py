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

        r=Reservation(
            refReservation=d["refReservation"][0],
            chargerAffaire=d["chargeAffaire"][0],
            dateReservation=d["dateReservation"][0],
            etat=False

        )
        r.save()
        
        g=list(d.items())
        c=dict(g[5:])
        print(d['refReservation'][0])
        
        # ref=Reservation.objects.filter(refReservation=d['refReservation'][0])[0]
      
        
        # for i in range(len(c['designation'])):
        #     f=DetilsReservation(
        #         refReservation=ref,
        #         designation=c['designation'][i],
        #         qte=c['qte'][i],
        #         dateLivraison=c['dateLivraison'][i],
        #         dateRetour=c['dateRetour'][i],



        #     )
            
        #     f.save()
        
      
    
    


    return render(request,'inventaire/reservations.html')


def stock(request):
    materiel=Stock.objects.all()
    print(materiel)
    return render(request,'inventaire/stock.html',{
        'title':"Inventaire",
        'materiel':materiel

    })

def detailStock(request, ref):

    mat=Stock.objects.filter(refMateriel=ref).values()[0]
    if (mat['categorie']=='GROUPE ELECTROGENE'):
        data=GroupeElectrogene.objects.filter(refMateriel=ref).values()[0]  
    elif (mat['categorie']=='CABINE AUTONOME'):
        data=CabinesAutonome.objects.filter(refMateriel=ref).values()[0]  
    else:
        data=Modulaire.objects.filter(refMateriel=ref).values()[0]  
            

    
        
    

    return render(request,"inventaire/detailStock.html",{
        'title':f"Detail de {ref}",
        'refrence':mat,
        'data':data,


    })

def addStock(request):
    req=request.POST

    print(req)
    return render(request,'inventaire/addstock.html',{
        'title': 'Ajtouer element',
    })