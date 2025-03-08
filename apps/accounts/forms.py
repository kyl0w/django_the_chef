from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
import re

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number']

    def clean_phone_number(self):
        """Custom validation for phone number"""
        phone_number = self.cleaned_data.get('phone_number')

        if not phone_number.isdigit():
            raise ValidationError("Numero de telefone deve conter apenas números.")

        if not re.match(r'^\d{9}$', phone_number):
            raise ValidationError("Deve conter 9 digitos.")

        return phone_number
