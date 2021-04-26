from django import forms
from bugs.models import CustomUser, Ticket


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class AddTicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)

class EditTicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    
class GenForm(forms.Form): 
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all())

class TicketStatusForm(forms.Form): 
    status = forms.ChoiceField(choices=[('new','new'),('in_process','in_process'),('finished','finished'),('invalid','invalid')])#savsasve and run!

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)