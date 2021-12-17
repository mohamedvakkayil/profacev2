from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Create your models here.
class prodir(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    jobsector=models.CharField(max_length=40)
    phone=models.BigIntegerField()
    workplace=models.CharField(max_length=40)
    reg_status=models.CharField(max_length=50)
    pr_status=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class unitdata(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name1=models.CharField(max_length=40)
    district=models.CharField(max_length=30)
    zone=models.CharField(max_length=40)
    unit=models.CharField(max_length=40)

    def __str__(self):
        return self.name1