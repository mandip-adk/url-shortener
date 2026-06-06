from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        
        form = RegisterForm()
    return render (request, "registration/register.html", {"form":form})
        
class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True

class CustomLogOutView(LogoutView):
    next_page= "login"




