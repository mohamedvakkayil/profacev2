from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class status(models.Model):
    mar=models.CharField(max_length=10)
    def __str__(self):
        return self.mar
class regddd(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.BigIntegerField()
    job=models.CharField(max_length=50,null=True,blank=True)
    district=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    ct=models.CharField(max_length=50,null=True,blank=True)
  
    
    def __str__(self):
        return '{}'.format(self.user)

class wife(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nm=models.CharField(max_length=50)
    ph=models.BigIntegerField(null=True,blank=True)
    pro=models.CharField(max_length=50,null=True,blank=True)
    age=models.IntegerField()
    children=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nm)

class st(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nm=models.CharField(max_length=50)
    age=models.IntegerField()




