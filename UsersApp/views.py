from django.shortcuts import render,redirect
from UsersApp.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def sign_up_view(request):
    if request.POST:
        #create an instance of sign-up form
        form=SignUpForm(request.POST or None)
        #validate form
        if form.is_valid():
            #save info to database
            new_user=form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"Hello {username} you signed up successfully")
            new_user=authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password1'])
            print("Succesful signup")
            login(request,new_user)
            return redirect("main:index")
    else:
        form=SignUpForm()
        
    context={
            'form':form,
    }
    return render(request,"UsersApp/sign-up.html",context)