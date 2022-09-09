from django.db import models
from accounts.models import Accounts
from projects.models import Project

# Create your models here.


class Manager(models.Model):
    account = models.OneToOneField(Accounts, on_delete=models.CASCADE)


class VP(models.Model):
    account = models.OneToOneField(Accounts, on_delete=models.CASCADE)
