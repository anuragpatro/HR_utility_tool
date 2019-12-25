from django.db import models
from main.models import Person
# Create your models here.
class Salary(models.Model):
    person = models.ForeignKey(Person,on_delete = models.CASCADE, null = True)
    basicpay = models.DecimalField(max_digits=9,decimal_places=2)
    hra = models.DecimalField(max_digits=9,decimal_places=2)    
    transport = models.DecimalField(max_digits=9,decimal_places=2)    
    medical = models.DecimalField(max_digits=9,decimal_places=2)    
    prof_update = models.DecimalField(max_digits=9,decimal_places=2)    
    special_allowance = models.DecimalField(max_digits=9,decimal_places=2)    
    prof_tax = models.DecimalField(max_digits=9,decimal_places=2)    
    variable_pay = models.DecimalField(max_digits=9,decimal_places=2)    
    PF = models.DecimalField(max_digits=9,decimal_places=2)    
    ESI = models.DecimalField(max_digits=9,decimal_places=2)    

    def __str__(self):
        return self.person.name + ' - Salary'
    
class monthly_salary(models.Model):
    person = models.ForeignKey(Person,on_delete = models.CASCADE,null = True)
    present_days = models.IntegerField(default = 0)
    month = models.CharField(max_length=10,null= True)
    year = models.IntegerField(null = True)

    def __str__(self):
        return (self.month + " " + str(self.year) + " - " + self.person.name)