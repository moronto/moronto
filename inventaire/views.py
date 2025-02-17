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
        
        req=request.POST

        currentYear=datetime.now().strftime("%Y").strip()
        global reservation
        
        reservation=Reservation.objects.all()
        print(reservation)
        refs=[]
        for r in reservation:
            print(type(r))
        print(refs)    
        if Reservation.objects.count()==0 or reservation['refReservation'][-4:]!=currentYear:
            refReservation = f'1-{currentYear}'

            print("ahya kighan dghi",refReservation)
        else:
            i=reservation['refReservation'].find('-')
            num=int(reservation['refReservation'][:i])

            refReservation=f'{num+1}-{currentYear}'
            print("anuk nit",refReservation)

        try:
            r=Reservation(refReservation=refReservation,
                        chargerAffaire=req.get('chargerAffaire'),
                        dateReservation=req.get('dateReservation'),
                        client=req.get('client'),
                        etat='En cours',
                        created_at=datetime.now(),
                        )
        
            r.save()
            refM=Reservation.objects.get(refReservation=refReservation)
            G=dict(req)
            l=len(G.get("designation"))
   
            for i in range(l):
                detil=DetilsReservation(refReservation=refM,
                                         designation=G.get("designation")[i],
                                         qte=G.get("qte")[i],
                                         dateLivraison=G.get("dateLivraison")[i],
                                         dateRetour=G.get("dateRetour")[i])
                detil.save()
            messages.success(request,f"Vous avez ajouter {refM} avec succes ")
        except Exception as e:
            messages.warning(request,f"une erreur est ce produit : {str(e)}") 
    charge=Chargesaffaire.objects.all()       
    return render(request,'inventaire/addreservation.html',{'charge':charge})
def editReservation(request , ref):
    reservation=Reservation.objects.get(refReservation=ref)
    detail=DetilsReservation.objects.filter(refReservation=ref)
    if request.method=='POST':
        req=request.POST
        print(req.get('chargerAffaire'))
        print(reservation.client)
        try:
            
            reservation.chargerAffaire=req.get('chargerAffaire')
            reservation.dateReservation=req.get('dateReservation')
            reservation.client=req.get('client')
            reservation.etat='En cours'
            reservation.created_at=datetime.now()
            reservation.save()
          
            # G=dict(req)
            # l=len(G.get("designation"))
   
            # for i in range(l):
            #     detail.designation=G.get("designation")[i]
            #     detail.qte=G.get("qte")[i]
            #     detail.dateLivraison=G.get("dateLivraison")[i]
            #     detail.dateRetour=G.get("dateRetour")[i]
            #     detail.save()
            messages.success(request,f"Vous avez Modifier {ref} avec succes ")
        except ValueError :
            messages.warning(request,f"une erreur est ce produit : ") 
    return render(request,'inventaire/editReservation.html',{
        'title': f'Modification de {ref}',
        'reservation': reservation,
        'charge':Chargesaffaire.objects.all(),
        'detail':detail,
    })
def reservations(request):
    
    data=Reservation.objects.all()
    if request.method=='POST':
        data=Reservation.objects.all()
    
    return render(request,'inventaire/reservations.html',{
        'title':'Reservations',
        'data':data,
        
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