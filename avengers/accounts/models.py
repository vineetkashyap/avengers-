from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from designation.models import Manager, VP
import hashlib

# Create your models here.

ACCOUNT_TYPE = (

    ("vp", "vp"),
    ("manager", "manager"),

)


class Manager(models.Models):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # account_type  =  models.CharField(max_length=50,choices = ACCOUNT_TYPE)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        pwd = make_password(self.password)
        self.password = pwd
        super(VP, self).save(*args, **kwargs)


class VP(models.Models):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # account_type  =  models.CharField(max_length=50,choices = ACCOUNT_TYPE)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        pwd = make_password(self.password)
        self.password = pwd
        super(VP, self).save(*args, **kwargs)
    #     if self.account_type == "vp":
    #         VP_acc = VP(self)
    #         VP_acc.save()
    #     elif self.account_type == "manager":
    #         Manager_acc = Manager(self)
    #         Manager_acc.save()
