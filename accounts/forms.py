# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        label="I am a",
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ("username", "email", "user_type", "password1", "password2")
