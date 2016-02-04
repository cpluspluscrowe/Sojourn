from django.db import models
from django.contrib.auth.models import  User # This is Django's built in User Class!
from django.db.models.signals import post_save
from django.dispatch import receiver
from check_manager.models import *

class Person(models.Model):
    corresponding_user = models.OneToOneField(User,unique = True)
    street = models.CharField(max_length = 50,null = True)
    city = models.CharField(max_length = 30,null = True)
    state = models.CharField(max_length = 20,null = True)
    zip_code = models.CharField(max_length = 5,null = True)
    #total_givings = models.DecimalField(max_digits=7, decimal_places=2)

@receiver(post_save,sender = User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        print("sender",sender,"instance",instance,"created",created)
        Person.objects.create(corresponding_user = instance)

post_save.connect(create_user_profile,sender = User)