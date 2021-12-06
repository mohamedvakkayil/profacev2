from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class caldir(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    jobsector=models.CharField(max_length=40)
    phone=models.BigIntegerField()
    panchayat=models.CharField(max_length=40)
    reg_status=models.CharField(max_length=50)
    pr_status=models.CharField(max_length=50)

    def __str__(self):
        return self.name