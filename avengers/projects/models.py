from django.db import models
from accounts.models import Manager
from developer.models import Developer


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=11)


class Request(models.Model):
    request_time = models.DateTimeField(auto_now=True, auto_now_add=False)


class Project(models.Model):
    name = models.CharField(max_length=50)
    brief = models.TextField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
