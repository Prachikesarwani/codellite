from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('index.html',views.index,name='home'),
    path('links.html',views.LINKS,name='LINKS'),
    path('cowin.html',views.COWIN,name='COWIN'),
    path('login.html',views.SIGN,name='SIGN'),
    path('index.html#REGISTER',views.REGISTER,name='REGISTER'),
    path('tnc.html',views.tnc,name='tnc'),
    path('contact.html',views.CONTACT,name='CONTACT'),
    path('new.html',views.registerbtn,name='registerbtn'),
    path('thanks.html',views.thanks,name='thanks'),
    path('logout',views.logoutuser,name="logout")
    

]