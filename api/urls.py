from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

route=DefaultRouter()

route.register('stock',StockData,basename="stock"),

urlpatterns = [
    path("",include(route.urls)),
        path('stocks/<str:ref>/', detailStock, name='stock-detail'),

]
