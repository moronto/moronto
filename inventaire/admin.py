from django.contrib import admin
from .models import *

class StockAdmin(admin.ModelAdmin):
    list_display=("refMateriel","designation","situation","lieu","categorie")

admin.site.register(Chargesaffaire)
admin.site.register(Reservation)
admin.site.register(DetilsReservation)
admin.site.register(Stock,StockAdmin)
admin.site.register(Modulaire)
admin.site.register(GroupeElectrogene)
admin.site.register(CabinesAutonome)
# Register your models here.
