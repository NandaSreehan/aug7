from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from app.models import lists
def home(request):
    a=lists.objects.all()[::-1]
    return render(request,'home.html',{'res':a})
def register(request):
    if request.method=='POST':
        usernam=request.POST.get('uname')
        firstnam=request.POST.get('fname')
        lastnam=request.POST.get('lname')
        emailnam=request.POST.get('mail')
        passwnam=request.POST.get('passw')
        cpasswnam=request.POST.get('cpass')
        if User.objects.filter(username=usernam):
            return redirect('loginpage')
        if len(passwnam)<8:
            return redirect('registerpage')
        if passwnam==cpasswnam:
            return redirect('registerpage')
        if len(usernam)<5:
            return redirect('registerpage')
        o=User(username=usernam,first_name=firstnam,last_name=lastnam,email=emailnam,password=passwnam)
        o.save()
    return render(request,'register.html')
def loginv(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method=='POST':
        userna=request.POST.get('uname')
        passwname=request.POST.get('passw')
        result=authenticate(request,username=userna,password=passwname)
        if result is not None:
            login(request,result)
            return redirect('profilepage')
        else:
            return redirect('loginpage')
    return render(request,'login.html')

@login_required(login_url='loginpage')
def profile(request):
    if request.user.is_superuser:
        return redirect('/admin')
    else:
        return render(request,'profile.html')
    
    

def mytweetview(request):
    if request.user.is_superuser:
        return redirect('/admin')
    a=lists.objects.all()[::-1]
    b=str(request.user.username)
    return render(request,'tweet.html',{'res':a,'usname':b})

def delete(request,rid):
    obj=lists.objects.filter(id=rid)
    obj.delete()
    return redirect('mytweetpage')

def update(request):
    return (request,'single.html')


@login_required(login_url='loginpage')
def create(request):
    if request.method=='POST':
        text=request.POST.get('pname')
        u=str(request.user.username)
        obj=lists(uname=u,post=text)
        obj.save()
    return render(request,'create.html')

def logoutv(request):
    logout(request)
    return redirect('loginpage')
