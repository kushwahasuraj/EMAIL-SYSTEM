from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, send_mail,send_mass_mail
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserLoginForm,UserRegisterForm
from django.contrib.auth import login ,authenticate ,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import  ValidationError

# Create your views here.
def home(request):
    return render(request,'home.html',{})
def base(request):
    return render(request,'base.html',{})


def LoginView(request):
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('/base')
        else:
            raise ValidationError('Invalid uname or password', code='invalid')
    return render(request,"login.html",{'form':form})

User=get_user_model()
def RegisterView(request):
    form=UserRegisterForm(request.POST or None)
    if form.is_valid():
        uname=form.cleaned_data.get("Username")
        email=form.cleaned_data.get("Email")
        passwd=form.cleaned_data.get("Password")
        User.objects.create_user(uname,email,passwd)
        return redirect('/login')
    return render(request,"register.html",{"form":form})

@login_required
def LogoutView(request):
    logout(request)
    return redirect('/base')

def send_email(request):
    subject = request.POST.get('subject','')
    message = request.POST.get('message','')
    to_email = (request.POST.get('from_email','')+" ").split()
    #print("subject",subject)
    #print("message", message)
    #print("to_email", to_email)
    if subject and message and to_email:
        send_mail(subject, message,'pankaj.ias543@gmail.com',to_email)
    else:
        print("error has occured")
        # In reality we'd use a form class
        # to get proper validation errors.
    return render(request, 'compose.html', {})

def password(request):
    return render(request,'password.html',{})

def main(request):
    return render(request,'main.html',{})

def main(request):
    return render(request,'main.html',{})

# def compose(request):
#     return render(request,'compose.html',{})
def sendemail(request):
    return render(request,'sendemail.py',{})




