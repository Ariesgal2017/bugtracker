from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username#save and test

class Ticket(models.Model):
    Possible_Statuses = [
        ('new', 'new'),
        ('in_process', 'in_process'),
        ('invalid', 'invalid'),
        ('finished', 'finished'),
    ]

    ticketstatus = models.CharField(max_length=25, choices=Possible_Statuses, default='new')  
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    filed_by = models.ForeignKey(CustomUser, related_name='filed', on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(CustomUser, related_name='ass', on_delete=models.CASCADE,null=True,blank=True)
    completed_by = models.ForeignKey(CustomUser, related_name='completedby', on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title or '' 

    #3 wat now i dont know what that other one is??? lol which one>>.thiS? ?O?N/e/