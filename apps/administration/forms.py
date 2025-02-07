from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import CustomUser
import os

class AdminSignupForm(UserCreationForm):
    admin_key = forms.CharField(
        max_length=100,
        help_text="Entre com a chave de administração fornecida.",
        widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'phone_number', 'password1', 'password2', 'admin_key')

    def clean_admin_key(self):
        key = self.cleaned_data.get('admin_key')
        expected_key = os.environ.get('ADMIN_KEY')
        if key != expected_key:
            raise forms.ValidationError("Chave de administração inválida.")
        return key

class AdminLoginForm(AuthenticationForm):
    admin_key = forms.CharField(
        max_length=100,
        help_text="Entre com a chave de administração fornecida.",
        widget=forms.PasswordInput
    )

    def clean(self):
        # Perform the standard authentication first.
        result = super().clean()
        key = self.cleaned_data.get('admin_key')
        expected_key = os.environ.get('ADMIN_KEY')
        if key != expected_key:
            raise forms.ValidationError("Chave de administração inválida.")
        return result
