from django import forms
from .models import *


class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields="__all__"

        widgets={
            'refReservation':forms.TextInput(attrs={"class":"form-control","pattern":"^\d+-\d+{8}$"}),
            'chargerAffaire':forms.TextInput(attrs={"class":"form-control"}),
            'dateReservation':forms.TextInput(attrs={"class":"form-control"}),
            'client':forms.TextInput(attrs={"class":"form-control"}),
            'etat':forms.TextInput(attrs={"class":"form-control"}),
        }
