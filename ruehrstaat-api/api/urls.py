from django.urls import path

from . import views

urlpatterns = [
    path('getAllCarriers', views.getAllCarriers.as_view(), name='getAllCarriers'),
    path('carrier', views.carrier.as_view(), name='carrier'),
    path('carrierJump', views.carrierJump.as_view(), name='carrierJump'),
]