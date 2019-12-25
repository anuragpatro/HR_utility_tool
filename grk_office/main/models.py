from django.db import models
import datetime

# Create your models here.
class Person(models.Model):
    name =  models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    qualification = models.CharField(max_length=20)
    dateofbirth = models.DateField()
    status_choices = [('yes','YES'),('no','NO')]
    status = models.CharField(max_length = 3,choices=status_choices)
    pannum = models.CharField(max_length=40)
    aadhar = models.BigIntegerField()
    laddress = models.CharField(max_length=60)
    paddress = models.CharField(max_length=60)
    designation = models.CharField(max_length=30,null=True)
    dateofjoin = models.DateField(null=True)

    def __str__(self):
        return self.name
