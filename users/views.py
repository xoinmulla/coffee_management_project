from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm  # Only import what you need

# Removed register_view and RegisterForm usage

class CustomPasswordResetView(PasswordResetView):
    """
    Custom view for handling password reset functionality.
    Uses a custom password reset form with Captcha.
    """
    form_class = CustomPasswordResetForm

def home_view(request):
    return render(request, 'home.html')
