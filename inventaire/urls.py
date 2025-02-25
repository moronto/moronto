from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('addreservation/',addreservation,name='addreservation'),
    path('reservations/',reservations,name='reservations'),
    path('reservations/<str:ref>',deleteReservation,name='deleteReservation'),
    path('detailReservation/<str:ref>',detailReservation,name='detailReservation'),
    path('detailReservation/<int:id>/<str:ref>',deleteDetailReservation,name='deleteDetailReservation'),
    path('editReservation/<str:ref>',editReservation,name='editReservation'),
    path('search/',searchReservation,name='search'),
    path('stock/',stock,name='stock'),
    path('detailStock/<str:ref>',detailStock,name='detailStock'),
    path('addstock/',addStock,name='addstock'),

]
