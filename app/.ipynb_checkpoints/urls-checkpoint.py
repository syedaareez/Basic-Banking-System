from django.contrib import admin
from django.urls import path
from app import views

app_name='app'

urlpatterns = [
    path('',views.home,name="home"),
    path('userlist/',views.userlist,name="userlist"),
    path('transaction/',views.transaction,name="transaction"),
    path('sendto/<str:pk>',views.sendto,name="sendto"),
    path('sendform/',views.history,name="sendform"),
]
