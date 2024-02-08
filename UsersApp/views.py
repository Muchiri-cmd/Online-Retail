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
            #login user to current sessions and redirect to home page
            login(request,new_user)
            return redirect("main:index")
    else:
        form=SignUpForm()
        
    context={
            'form':form,
    }
    return render(request,"UsersApp/sign-up.html",context)

def sign_in_view(request):
    #if request.user.is_authenticated:
        #return redirect("main:index")
    
    if request.method == "POST": 
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Check if user exists
            user = User.objects.get(email=email)
           
            if user is not None:
                authenticated_user=authenticate(request,email=email,password=password)
                print("User account present")
                if authenticated_user is not None:
                    print("User authenticated successfully")
                    login(request, user)
                    messages.success(request, "You're successfully logged in")
                    return redirect("main:index")
                else:
                    print("authentication failed")
        except User.DoesNotExist:
            print("User not registered")
            messages.warning(request, "User not registered.")
        except:
            print("Something went wrong. Please try again.")
            messages.warning(request, "Something went wrong. Please try again.")

    return render(request, "UsersApp/sign-in.html")
