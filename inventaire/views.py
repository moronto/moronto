from django.shortcuts import render,redirect
from django.urls import reverse
import json
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from .models import *
from django.contrib import messages
from .forms import *
from datetime import timezone,datetime
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'inventaire/home.html',{
        'title':"ATOULOC"
    })

#views of gestion reservation
@login_required
def addreservation(request):
    if request.method=='POST':
        
        req=request.POST
        
        currentYear=datetime.now().strftime("%Y").strip()
        refs=[]
        reservation=Reservation.objects.all()
        if reservation.count() != 0:
            print('hayi',reservation.count)
            for r in reservation:
                refs.append(int(r.refReservation.split('-')[0]))
            refReservation=f'{max(refs)+1}-{currentYear}'
        else:    
            refReservation=f'1-{currentYear}'


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
            print(G.get("designation"))
            l=len(G.get("designation"))
   
            for i in range(l):
                detil=DetilsReservation(refReservation=refM,
                                         designation=G.get("designation")[i],
                                         qte=G.get("qte")[i],
                                         dateLivraison=G.get("dateLivraison")[i],
                                         dateRetour=G.get("dateRetour")[i])
                detil.save()
            messages.success(request,f"Vous avez ajouter {refM} avec succes ")
            return redirect("reservations")
        except Exception as e:
            messages.warning(request,f"une erreur est ce produit : {e}") 
    charge=Chargesaffaire.objects.all()       
    return render(request,'inventaire/addreservation.html',{'charge':charge})
@login_required
def editReservation(request , ref):
    reservation=Reservation.objects.get(refReservation=ref)
    detail=DetilsReservation.objects.filter(refReservation=ref)
    if request.method=='POST':
        req=request.POST
       
      
        try:
            
            reservation.chargerAffaire=req.get('chargerAffaire')
            reservation.dateReservation=req.get('dateReservation')
            reservation.client=req.get('client')
            reservation.etat=req.get('etat')
            reservation.created_at=datetime.now()
            reservation.save()

            DetilsReservation.objects.filter(refReservation=ref).delete()
            G=dict(req)
            l=len(G.get("designation"))
            print(reservation.refReservation,type(reservation))
            for i in range(l):
                detil=DetilsReservation(refReservation=reservation,
                                         designation=G.get("designation")[i],
                                         qte=G.get("qte")[i],
                                         dateLivraison=G.get("dateLivraison")[i],
                                         dateRetour=G.get("dateRetour")[i])
                detil.save()
            messages.success(request,f'Vous avez modifier information de reservation : {ref}') 
            return redirect('reservations')   
          
         
          
        except  Exception as e :
            messages.warning(request,f"une erreur est ce produit : {e}") 
    return render(request,'inventaire/editReservation.html',{
        'title': f'Modification de {ref}',
        'reservation': reservation,
        'charge':Chargesaffaire.objects.all(),
        'detail':detail,
    })
@login_required
def reservations(request):
    
    data=Reservation.objects.all()
    if request.method=='POST':
        data=Reservation.objects.all()
    
    return render(request,'inventaire/reservations.html',{
        'title':'Reservations',
        'data':data,
        
    })
@login_required
def deleteReservation(request, ref):
    r=Reservation.objects.get(refReservation=ref)
    r.delete()
    return redirect("reservations")
@login_required
def deleteDetailReservation(request, id,ref):
    r=DetilsReservation.objects.get(id=id)
    r.delete()
    return redirect(f"/detailReservation/{ref}")
@login_required
def searchReservation(request):
    if request.method=='GET':
       if request.GET.get('valSearch')=='':
            data=Reservation.objects.all()
       else:    
          data=Reservation.objects.filter(Q(refReservation__icontains=request.GET.get('valSearch'))|
                                          Q(dateReservation__icontains=request.GET.get('valSearch'))|
                                          Q(chargerAffaire__icontains=request.GET.get('valSearch'))|
                                          Q(client__icontains=request.GET.get('valSearch'))|
                                          Q(etat__icontains=request.GET.get('valSearch'))
                                          )
          

       results = [
        {
            'dateReservation': dt.dateReservation.strftime('%d/%m/%Y'),
            'refReservation': dt.refReservation,
            'chargerAffaire': dt.chargerAffaire,
            'client': dt.client,
            'etat': dt.etat,
            'urlDetails':reverse('detailReservation',args=[dt.refReservation]),
            'urlEdit':reverse('editReservation',args=[dt.refReservation]),
            'urlDelete':reverse('deleteReservation',args=[dt.refReservation]),
        }
        for dt in data
                ]
       return JsonResponse({'data':results})

# views of gestion stock

@login_required
def stock(request):
    materiel=Stock.objects.all()
    
    return render(request,'inventaire/stock.html',{
        'title':"Inventaire",
        'materiel':materiel

    })
@login_required
def detailReservation(request,ref):
    r=DetilsReservation.objects.filter(refReservation=ref)
    print(r)

    return render(request,"inventaire/detailReservation.html",{'title':'Details Reservation', 'reservation':r})
@login_required
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
@login_required
def addStock(request):


    if request.method =='POST':
        st=Stock(refMateriel=request.POST.get("refMateriel"),
                designation=request.POST.get("designation"),
                situation='DISPONIBLE',
                lieu=request.POST.get("lieu"),
                categorie=request.POST.get("categorie"))
        if Stock.objects.filter(refMateriel=request.POST.get("refMateriel")).exists():
            messages.warning(request,f"Pardon ce Réference {request.POST.get('refMateriel')} existe déja")
        else :    
            st.save()
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
            messages.success(request,f"Vous avez ajouter {request.POST.get('refMateriel')} avec succés")
            return redirect('stock')
    
    return render(request,'inventaire/addstock.html',{
        'title': 'Ajtouer element',
                  })

# views of movement
def movement(request):
    data=Movement.objects.all()

    return render(request,"inventaire/movements.html",{'data':data})
def searchMovement(request):
    if request.method=='GET':
       if request.GET.get('valSearch')=='':
            data=Movement.objects.all()
       else:    
          data=Movement.objects.filter(Q(refMateriel__icontains=request.GET.get('valSearch'))|
                                          Q(designation__icontains=request.GET.get('valSearch'))|
                                          Q(client__icontains=request.GET.get('valSearch'))|
                                          Q(dateMovement__icontains=request.GET.get('valSearch'))|
                                          Q(typeMovement__icontains=request.GET.get('valSearch'))
                                          )
          

       results = [
        {
            'typeMovement': dt.typeMovement,
            'dateMovement': dt.dateMovement.strftime('%d-%m-%Y'),
            'refMateriel': dt.refMateriel,
            'designation': dt.designation,
            'client': dt.client,
            'urlDetails':reverse('detailReservation',args=[dt.id]),
            'urlDelete':reverse('deleteReservation',args=[dt.id]),
        }
        for dt in data
                ]
       return JsonResponse({'data':results})
def detailMovement(request,id):
    data=Movement.objects.filter(id=id).values()[0]

    return render(request,"inventaire/detailMovement.html",{'data':data})
def addMovement(request):
    materiel=Stock.objects.all()
    if request.method =='POST':    
        move=Movement(
                        typeMovement=request.POST.get("typeMovement"),
                        dateMovement=request.POST.get("dateMovement"),
                        typeLocation=request.POST.get("typeLocation"),
                        depot=request.POST.get("depot"),
                        refMateriel=request.POST.get("refMateriel"),
                        designation=request.POST.get("designation"),
                        qte=request.POST.get("qte"),
                        client=request.POST.get("client"),
                        lieu=request.POST.get("lieu"),
                        matTrans=request.POST.get("matTrans"),
                        condTrans=request.POST.get("condTrans"),
                        observations=request.POST.get("observations"),
                )
                    

        move.save()
        messages.success(request,f"Vous avez ajouter  {request.POST.get('typeMovement')} de {request.POST.get('refMateriel')} avec success")
        return redirect('movement')       
        
    

    return render(request,"inventaire/addMovement.html",{

        'title':'Ajouter Mouvement',
        'materiel':materiel,
        'client':['SOGEA','NGE','TGCC','AVANT SCENE','ACWA POWER','SENER']

    })


def searchDesignation(request):
    if request.method=='GET':
       da={}  
       dispo=""
       lieu=request.GET.get('lieu')
       typeMove=request.GET.get('typeMovement')
       data=Stock.objects.filter(refMateriel=request.GET.get('valSearch'))
       for d in data:
            
            print(lieu , typeMove)
            if d.situation=='DISPONIBLE' and typeMove=='SORTIE':
                data.update(situation='LOUER' )
                data.update(lieu=lieu)
            elif d.situation=='LOUER' and typeMove=='ENTREE':
                data.update(situation='DISPONIBLE',lieu=" ")
            elif d.situation=='LOUER' and typeMove=='SORTIE':
                print("kighen ghida 1")
                dispo='louer'
            elif d.situation=='DISPONIBLE' and typeMove=='ENTREE':
                dispo='dispo'

        

            
            da= {"designation":d.designation,
                 'dispo':dispo}

       return JsonResponse({'data':da})
    
def deleteMovement(request, id):
    move=Movement.objects.get(id=id)
    move.delete()

    messages.info(request, f"Vous avez supprimer {move} avec success")   
    return redirect("movement") 
    

    