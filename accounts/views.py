# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("accounts:profile")  # or your landing page
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")


@login_required
def profile_view(request):
    # You can pass user info to the template if you like
    return render(request, "accounts/profile.html")
