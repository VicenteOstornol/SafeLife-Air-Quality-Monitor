from email.policy import default
import uuid
from django.db import models
#uid = models.AutoField(primary_key=True)
# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=254)

class DeviceModel(models.Model):
    mac_ad = models.CharField(primary_key=True,max_length=17) 

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=50, null=True)
    nombre = models.CharField(max_length=50, null=True)
    edad = models.CharField(max_length=50, null=True)
    contacto = models.CharField(max_length=50, null=True)
    condicion = models.CharField(max_length=50, null=True)

class DevicePatient(models.Model):
    id_Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    id_Device = models.CharField(max_length=50, null=True)
