from django.db import models
from django.conf import settings

class victim(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    password = models.CharField(max_length=32)

class police(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ph_no=models.CharField(max_length=10)
    police_station=models.CharField(max_length=30)
    is_head=models.BooleanField(default=False)


class case(models.Model):
    descreption=models.TextField(default="") 
    status=models.CharField(max_length=50,default="")
    head_description=models.TextField(default="")
    police_station=models.CharField(max_length=30)    

class pol_case(models.Model):
    case=models.ForeignKey(case, related_name='pol_case',on_delete=models.CASCADE)
    police=models.ForeignKey(police, related_name='police',on_delete=models.CASCADE)
    #victim=models.ForeignKey(victim, related_name='victim',on_delete=models.CASCADE)        

  
class vic_case(models.Model):
    case=models.ForeignKey(case, related_name='vic_case',on_delete=models.CASCADE)
    victim=models.ForeignKey(victim, related_name='victim',on_delete=models.CASCADE)        

class case_images(models.Model):
    case=models.ForeignKey(case, related_name='images',on_delete=models.CASCADE)
    image=models.ImageField()  
