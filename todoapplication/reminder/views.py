from django.shortcuts import render,redirect

from django.views.generic import View
from reminder.forms import UserForm,LoginForm
from django.contrib.auth import authenticate,login,logout 

# Create your views here.


class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=UserForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("account created")
            return redirect("register")
        else:
            print("failed")
            return render(request,"register.html",{"form":form})
        
class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                print("login sucess")
                return redirect("index")
        print("invalid")
        return render(request,"login.html",{"form":form})

class IndexView(View):
   def get(self,request,*args,**kwargs):
        
        return render(request,"index.html")
