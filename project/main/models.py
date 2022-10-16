import uuid
from django.db import models
#uid = models.AutoField(primary_key=True)
# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254)
