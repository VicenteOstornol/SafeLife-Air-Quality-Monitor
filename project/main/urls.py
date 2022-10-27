from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_netatmo/', views.login_netatmo, name='login_netatmo'),
    path('logout/', views.logout, name='logout'),
    path('autorize/', views.autorize, name='autorize'),
    path('devices/', views.devices, name='devices'),
    path('create_patient/', views.create_patient, name='createPatient'), #Testear
    path('patients/', views.read_patient, name='patients'), #Testear
    path('update_patient/<int:pk>', views.update_patient, name='updatePatient', ), #Testear
    path('delete/<int:pk>',views.delete_patient,name='delete')
]