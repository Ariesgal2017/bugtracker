from django.contrib import admin
from bugs.models import CustomUser,Ticket
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Ticket)