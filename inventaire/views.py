from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
from datetime import timezone,datetime
def home(request):
    return render(request,'inventaire/home.html',{
        'title':"ATOULOC"
    })

def login(request):
    return render(request,'inventaire/login.html')

def addreservation(request):
    if request.method=='POST':
        currentYear=datetime.now().strftime("%Y").strip()
        reservation=Reservation.objects.all()
        if reservation.count()==0:
            refReservation = f'1-{currentYear}'
            print(refReservation)
        print('izrid win yadawen')


    return render(request,'inventaire/addreservation.html')
def addreservationA(request):
    refReservation=''
    req=request.POST
    lastRef=Reservation.objects.all().order_by("created_at").last().__str__()
    print('this is ',lastRef, f'and {type(lastRef)}')
    actualYear=datetime.now().strftime("%Y").strip()
    if  lastRef== 'None':
        raise ValueError('La badse de donnes est vide') 
    # i=lastRef.find('-')
    # beginRef=int(lastRef[:i])
    # if  lastRef[i+1:] == actualYear:
    #     beginRef+=1
    #     refReservation=f"{beginRef}-{actualYear}"
        
        
    # else: 
    #     beginRef=1
    #     refReservation=f"{beginRef}-{actualYear}"
        
    if request.method=='POST':
        if Reservation.objects.filter(refReservation=req.get('refReservation')).exists():
            messages.warning(request,f'la reservation {refM} est deja exite ')
            exit
        else:
            r=Reservation(refReservation=refReservation,
                        chargerAffaire=req.get('chargerAffaire'),
                        dateReservation=req.get('dateReservation'),
                        client=req.get('client'),
                        etat='En cours',
                        created_at=datetime.now(),
                        )
        
            r.save()
        messages.success(request,f"Vous avez ajouter {req.get('refReservation')} avec succes ")
        G=dict(req)

        refM=Reservation.objects.get(refReservation=refReservation)
        l=len(G.get("designation"))
   
        for i in range(l):
             if Reservation.objects.filter(refReservation=refM).exists():
                    messages.warning(request,f'La reservation {refM} est deja existe ')
                    break
             else:
                detil=DetilsReservation(refReservation=refM,
                                            designation=G.get("designation")[i],
                                            qte=G.get("qte")[i],
                                            dateLivraison=G.get("dateLivraison")[i],
                                            dateRetour=G.get("dateRetour")[i])
                detil.save()
    charge=Chargesaffaire.objects.all()
    return render(request,'inventaire/addreservation.html',{'charge':charge})

def reservations(request):
    
    data=Reservation.objects.all()
    if request.method=='POST':
        data=Reservation.objects.all()
    
    return render(request,'inventaire/reservations.html',{
        'title':'Reservations',
        'data':data
    })
def deleteReservation(request, ref):
    r=Reservation.objects.get(refReservation=ref)
    r.delete()
    return redirect("reservations")
def deleteDetailReservation(request, id,ref):
    r=DetilsReservation.objects.get(id=id)
    r.delete()
    return redirect(f"/detailReservation/{ref}")
def stock(request):
    materiel=Stock.objects.all()
    
    return render(request,'inventaire/stock.html',{
        'title':"Inventaire",
        'materiel':materiel

    })
def detailReservation(request,ref):
    r=DetilsReservation.objects.filter(refReservation=ref)
    print(r)

    return render(request,"inventaire/detailReservation.html",{'title':'Details Reservation', 'reservation':r})

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