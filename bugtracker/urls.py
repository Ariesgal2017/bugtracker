"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bugs import views

# you need to define its path here! its not defined!
# the issue here its not even tying to run the index_view
# i might have found something
urlpatterns = [
    path('', views.index_view, name='home'),
    path('accounts/' , views.login_view, name='loginpage'),#save and try
    path('login/', views.login_view, name='loginpage'),
    path('logout/', views.logout_view, name='logoutpage'),
    path('tickets/add/', views.addticket_view),
    path('edit/<int:ticket_id>/', views.editticket_view, name='edittick'),
    path('user/<int:user_id>/', views.userdetail_view, name='user_detail'),
    path('tickets/<int:user_filed_id>/', views.ticketdetail_view,name='ticket_detail'),
    path('assignperson/<int:ticket_id>/', views.ticketassignuser_view, name='assign_ticket'), # wrong view!oops
    path('assignstatus/<int:ticket_id>/', views.ticketassignstatus_view, name='assign_status'), # wrong view!oops
   # path('complete/<int:ticket_id/', views.completedticket_view),
    # path('assignperson/<int:ticket_id>/', views.ticketstatus_view,name='statusview'),
    path('admin/', admin.site.urls),
]

#3now we need a new path to assignstatus just like we didi with assign person
#3inside w will have a if to eacho of the states, this way you wont need a lot of viewsok
