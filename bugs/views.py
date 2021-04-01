from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render, reverse

from bugs.forms import LoginForm, AddTicketForm, EditTicketForm, GenForm, TicketStatusForm
from bugs.models import CustomUser, Ticket

# Create your views here.


@login_required
def index_view(request):
    user = CustomUser.objects.all()
    ticket = Ticket.objects.all()
    new_ticket = Ticket.objects.filter(ticketstatus="new")
    in_process = Ticket.objects.filter(ticketstatus="in_process")
    finished = Ticket.objects.filter(ticketstatus="finished")
    invalid = Ticket.objects.filter(ticketstatus="invalid")
    
    
    print("Index View rendering")
    return render(request, 'index.html', {
        'user': user,
        'ticket': ticket,
        'new': new_ticket,
        'in_process': in_process,
        'finished': finished,
        'invalid': invalid,
    }
    )

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', reverse('loginpage')))


def addticket_view(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket = Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                filed_by=request.user 
            )
            print(ticket.id)
            return HttpResponseRedirect(reverse('home'))
    form = AddTicketForm()
    return render(request, html, {'form': form})


def ticketstatus_view(request, ticket_id):
    my_ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = GenForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_ticket.user_assigned = data['user']
            my_ticket.ticketstatus = 'in_process'
            my_ticket.save()
        return HttpResponseRedirect(reverse('home'))


def ticketdetail_view(request, user_filed_id):
    ticket_details = Ticket.objects.get(id=user_filed_id)
    person = GenForm(initial={'user':ticket_details.assigned_user})
    status = TicketStatusForm(initial={'status': ticket_details.ticketstatus})
    print( ticket_details.filed_by )
    return render(
        request, 'ticket_detail.html', {
            'ticket_detail': ticket_details, 'person': person, 'statusform':status}#3
    )


def userdetail_view(request, user_id):
    user = CustUser.objects.filter(id=user_id).first()
    userticket = Ticket.objects.filter(user_filed=user)
    return render(
        request, 'user_detail.html', {
            'user': user, 'userticket': userticket}
    )


def editticket_view(request, ticket_id):
    context = {}
    html = 'generic_form.html'
    edit = Ticket.objects.get(id=ticket_id) 
    if request.method == 'POST':
        form = EditTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print( data )
            edit.title = data.get('title')
            edit.description = str(data['description'])
            edit.save()
            return HttpResponseRedirect(reverse('home'))
    form = EditTicketForm(
        initial={'title': edit.title, 'description': edit.description}
    ) 
    context.update({'form': form})
    return render(request, html, context)

def ticketassignuser_view(request, ticket_id):  
    context = {}
    ticket = Ticket.objects.get(id=ticket_id) 
    if request.method == 'POST':
        form = GenForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data) 
            ticket.assigned_user = data.get('user') 
            ticket.ticketstatus = "in_process"
            ticket.completed_by = None
            ticket.save()
            return HttpResponseRedirect(reverse('home'))

def ticketassignstatus_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id) 
    if request.method == 'POST':
        form = TicketStatusForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticketstatus = data['status']
            if ticketstatus == "invalid":
                ticket.assigned_user = None 
                ticket.user_completed = None
                ticket.ticketstatus = 'invalid'
            elif ticketstatus == "finished":
                ticket.assigned_user = None
                ticket.user_completed = ticket.assigned_user
                ticket.ticketstatus = 'finished'
            else:
                ticket.ticketstatus = ticketstatus
            ticket.save()
    return HttpResponseRedirect(reverse('home'))
