from django.shortcuts import render
from .models import Users,History
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,"home.html")

def userlist(request):
    users=Users.objects.all()
    return render(request,"userlist.html",{'allusers':users})

def transaction(request):
    allh=History.objects.all()
    return render(request,"transaction.html",{'allhistory':allh})

def sendto(request,pk):
    user=Users.objects.get(id=pk)
    users=Users.objects.exclude(id=pk)
    return render(request,"sendto.html",{'user':user,'allUsers':users})

def successful(request):
    return render(request,"successful.html")

def failure(request):
    return render(request,"failure.html")

def history(request):
    if request.method=='POST':
        fromm=request.POST.get('sendfrom')
        to=request.POST.get('sendto')
        amt=request.POST.get('amount')
        userfrom=Users.objects.get(name=fromm)
        userto=Users.objects.get(name=to)
        flag=False
        
        if(amt):
            try:
                if(int(userfrom.balance)-int(amt)>=0):
                    history = History(sendfrom = fromm,sendto=to,amount=amt)
                    userfrom.balance=str(int(userfrom.balance)-int(amt))
                    userto.balance=str(int(userto.balance)+int(amt))

                    history.save()
                    userfrom.save()
                    userto.save()

                    receipt=History.objects.last()

                    return render(request,'successful.html',{'receipt':receipt,'fromuser':userfrom,'touser':userto})
                else:
                    flag=True
                    return render(request,'failure.html',{"flag":flag})
            except:
                return render(request,'failure.html',{"flag":flag})
        else:
            return render(request,'failure.html',{"flag":flag})
    else:
        return render(request,'transaction.html')