from django.contrib import admin

from .models import Client
from .models import Request
from .models import Project
# Register your models here.


admin.site.register(Client)
admin.site.register(Request)
admin.site.register(Project)
