from django import forms
from django.contrib.auth.forms import PasswordResetForm
from captcha.fields import CaptchaField

class CustomPasswordResetForm(PasswordResetForm):
    captcha = CaptchaField()  # Add Captcha field for password reset
