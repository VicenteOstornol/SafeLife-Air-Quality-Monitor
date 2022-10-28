from django.db import models
#uid = models.AutoField(primary_key=True)
# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=254)

class DeviceModel(models.Model):
    mac_ad = models.CharField(primary_key=True,max_length=17)
    station_name = models.CharField(unique=True, max_length=50,null=True)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=50, null=True, unique=True)
    nombre = models.CharField(max_length=50, null=True)
    edad = models.CharField(max_length=50, null=True)
    numero_contacto = models.CharField(max_length=50, null=True)
    nombre_contacto = models.CharField(max_length=50, null=True)
    condicion = models.CharField(max_length=50, null=True)
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE, null=True)



