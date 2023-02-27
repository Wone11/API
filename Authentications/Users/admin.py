from django.contrib import admin
from .models import Users, MASUsers, Clients

# Register your models here.
admin.site.register(Users)
admin.site.register(MASUsers)
admin.site.register(Clients)