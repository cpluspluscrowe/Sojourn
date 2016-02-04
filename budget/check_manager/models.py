from django.db import models
from django.contrib.auth.models import  User
import datetime
from datetime import date, datetime
today = date.today()
from person_manager.models import Person
class Check(models.Model):
    person = models.ForeignKey(Person,related_name = "check_giver",null = False, blank = False)
    amount = models.DecimalField(max_digits=7, decimal_places=2,null = False, blank = False)
    number = models.IntegerField(null = False)
    purpose = models.CharField(max_length = 30,null = True, blank = True)

class Cash(models.Model):
    person = models.ForeignKey(Person,related_name = "cash_giver",null = True, blank = True)
    amount = models.DecimalField(max_digits=7, decimal_places=2,null = False, blank = False)
    purpose = models.CharField(max_length = 30,null = True, blank = True)
