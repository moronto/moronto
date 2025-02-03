from django.shortcuts import render
from .models import *
from django.contrib import messages
def home(request):
    return render(request,'inventaire/home.html',{
        'title':"ATOULOC"
    })

def login(request):
    return render(request,'inventaire/login.html')


def reservations(request):

    req=request.POST
    if request.method=='POST':
       r=Reservation(refReservation=req.get('refReservation'),
                     chargerAffaire=req.get('chargerAffaire'),
                     dateReservation=req.get('dateReservation'),
                     client=req.get('client'),
                     etat='En cours',
                     )
       if Reservation.objects.filter(refReservation=req.get('refReservation')).exists():
            messages.warning(request,f"Pardon {req.get('refReservation')} exist deja ")
       else :
            r.save()
            messages.success(request,f"Vous avez ajouter {req.get('refReservation')} avec succes ")
            G=dict(req)

            refM=Reservation.objects.filter(refReservation=req.get('refReservation'))[0]
            l=len(G.get("designation"))
            print(refM)
           
            for i in range(l):
                detil=DetilsReservation(refReservation=refM,
                                        designation=G.get("designation")[i],
                                        qte=G.get("qte")[i],
                                        dateLivraison=G.get("dateLivraison")[i],
                                        dateRetour=G.get("dateRetour")[i])
                print(i)
                detil.save()

      
               

    


    return render(request,'inventaire/reservations.html')


def stock(request):
    materiel=Stock.objects.all()
    
    return render(request,'inventaire/stock.html',{
        'title':"Inventaire",
        'materiel':materiel

    })

def detailStock(request, ref):

    mat=Stock.objects.filter(refMateriel=ref).values()[0]
    if (mat['categorie']=='GROUPE ELECTROGENE'):
        data=GroupeElectrogene.objects.filter(refMateriel=ref).values()[0]  
    elif (mat['categorie']=='CABINES AUTONOMES'):
        data=CabinesAutonome.objects.filter(refMateriel=ref).values()[0]  
    else:
        data=Modulaire.objects.filter(refMateriel=ref).values()[0]  
            

    
        
    

    return render(request,"inventaire/detailStock.html",{
        'title':f"Detail de {ref}",
        'refrence':mat,
        'data':data,


    })

def addStock(request):
    print(request.POST)
    if request.method =='POST':
        st=Stock(refMateriel=request.POST.get("refMateriel"),
                designation=request.POST.get("designation"),
                situation=request.POST.get("situation"),
                lieu=request.POST.get("lieu"),
                categorie=request.POST.get("categorie"))
        if Stock.objects.filter(refMateriel=request.POST.get("refMateriel")).exists():
            messages.warning(request,f"Pardon ce Réference {request.POST.get('refMateriel')} existe déja")
        else :    
            st.save()
            messages.success(request,f"Vous avez ajouter {request.POST.get('refMateriel')} avec succés")
            ref=Stock.objects.filter(refMateriel=request.POST.get("refMateriel"))[0]
       
            if request.POST.get("categorie")=="GROUPE ELECTROGENE" :
                 ge=GroupeElectrogene(puissance=request.POST.get("puissance"),
                                 marque=request.POST.get("marque"),
                                 dimension=request.POST.get("dimensionGE"),
                                 refMateriel=ref)
                 ge.save()
            
            if request.POST.get("categorie")=="MODULAIRE" :
                modulaire=Modulaire(gamme=request.POST.get("gammeModulaire"),
                                    dimension=request.POST.get("dimensionModulaire"),
                                    refMateriel=ref)
                modulaire.save()    
            
            if request.POST.get("categorie")=="CABINES AUTONOMES" :
                cabine=CabinesAutonome(gamme=request.POST.get("gammeCabine"),
                                    dimension=request.POST.get("dimensionCabine"),
                                    color=request.POST.get("color"),
                                    refMateriel=ref)
                cabine.save()
    
    return render(request,'inventaire/addstock.html',{
        'title': 'Ajtouer element',
    })