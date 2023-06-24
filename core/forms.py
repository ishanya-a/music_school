from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=False, validators=[MinLengthValidator(2)])
    email = forms.EmailField()
    password = forms.CharField(label="password",
        strip=False,
        widget=forms.PasswordInput,validators=[MinLengthValidator(8)])
    password2 = forms.CharField(label="password2",
        widget=forms.PasswordInput,
        strip=False,)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_pass(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match.")

    def clean_username(self):
        username = self.cleaned_data.get('username')
    
        # Perform custom validation for the first name field
        if username:
            # Example validation: Ensure the first name contains only alphabetic characters
            if not username.isalpha():
                raise forms.ValidationError("First name should contain only alphabetic characters.")
    
        return username
