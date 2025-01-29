from django.contrib import admin
from .models import *

class StockAdmin(admin.ModelAdmin):
    list_display=("refMateriel","designation","situation","lieu","categorie")
admin.site.register(Stock,StockAdmin)

class ChargesaffaireAdmin(admin.ModelAdmin):
    list_display=("name","email","phone")
admin.site.register(Chargesaffaire,ChargesaffaireAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display=("refReservation","chargerAffaire","dateReservation","etat")
admin.site.register(Reservation,ReservationAdmin)

class DetilsReservationAdmin(admin.ModelAdmin):
    list_display=("refReservation","designation","qte","dateLivraison","dateRetour")
admin.site.register(DetilsReservation,DetilsReservationAdmin)

class ModulaireAdmin(admin.ModelAdmin):
    list_display=("gamme","dimension","refMateriel")
admin.site.register(Modulaire,ModulaireAdmin)

class GroupeElectrogeneAdmin(admin.ModelAdmin):
    list_display=("puissance","marque","dimension","refMateriel")
admin.site.register(GroupeElectrogene,GroupeElectrogeneAdmin)

class CabinesAutonomeAdmin(admin.ModelAdmin):
    list_display=("gamme","dimension","color","refMateriel")
admin.site.register(CabinesAutonome,CabinesAutonomeAdmin)
# Register your models here.
