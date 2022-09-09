from django.db import models
from manager.models import Manager
from developers.models import Developer


# Create your models here.
class Project(models.Models):
    name = models.CharField(max_length=50)
    brief = models.TextField()
    manager = models.ManytoOneField(Manager, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)


class Client(models.Models):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=11)


class Request(models.Model):
    request_time = models.DateTimeField(auto_now=True, auto_now_add=False)
