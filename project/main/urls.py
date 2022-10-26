from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_netatmo/', views.login_netatmo, name='login_netatmo'),
    path('logout/', views.logout, name='logout'),
    path('autorize/', views.autorize, name='autorize'),
    path('devices/', views.devices, name='devices'),
    path('create_patient/', views.create_patient, name='createPatient'), #Testear
    path('read_patient/', views.read_patient, name='patientList'), #Testear
    path('update_patient/', views.update_patient, name='updatePatient'), #Testear
]