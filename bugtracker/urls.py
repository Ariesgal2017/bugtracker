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

urlpatterns = [
    path('', views.index_view, name='home'),
    path('register', views.new_user_view, name='register'),
    path('accounts/' , views.login_view, name='loginpage'),
    path('login/', views.login_view, name='loginpage'),
    path('logout/', views.logout_view, name='logoutpage'),
    path('tickets/add/', views.addticket_view),
    path('edit/<int:ticket_id>/', views.editticket_view, name='edittick'),
    path('user/<int:user_id>/', views.userdetail_view, name='user_detail'),
    path('tickets/<int:user_filed_id>/', views.ticketdetail_view,name='ticket_detail'),
    path('assignperson/<int:ticket_id>/', views.ticketassignuser_view, name='assign_ticket'), # wrong view!oops
    path('assignstatus/<int:ticket_id>/', views.ticketassignstatus_view, name='assign_status'), # wrong view!oops
  
    path('admin/', admin.site.urls),
]

