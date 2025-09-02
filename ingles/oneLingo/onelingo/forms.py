from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Usuário')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Senha')

class CadastroForm(forms.Form):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Usuário')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Senha')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirmar Senha')
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Nome')
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Sobrenome')


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "As senhas não coincidem.")

        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            self.add_error(None, "Este campo é obrigatório.")
        if User.objects.filter(username=username).exists():
            self.add_error(None, "Este nome de usuário já está em uso.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            self.add_error(None, "Este campo é obrigatório.")
        if User.objects.filter(email=email).exists():
            self.add_error(None, "Este email já está em uso.")
        return email
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            self.add_error(None, "Este campo é obrigatório.")
        if first_name.isnumeric():
            self.add_error(None, "O nome não pode ser numérico.")
        if len(first_name) < 3:
            self.add_error(None, "O nome deve ter pelo menos 3 caracteres.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name:
            self.add_error(None, "Este campo é obrigatório.")
        if last_name.isnumeric():
            self.add_error(None, "O sobrenome não pode ser numérico.")
        if len(last_name) < 3:
            self.add_error(None, "O sobrenome deve ter pelo menos 3 caracteres.")
        return last_name
