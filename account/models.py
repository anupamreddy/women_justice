from django.db import models
from django.conf import settings

# Create your models here.
class victim(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    password = models.CharField(max_length=32)

class police(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ph_no=models.CharField(max_length=10)







