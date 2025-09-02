from urllib import response
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CadastroForm, CustomLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction
import uuid

class HomeView(TemplateView):
    template_name = 'home.html' 
    def post(self, request, *args, **kwargs):
        user_id = uuid.uuid4()[:40]
        
        return redirect('login')


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = CustomLoginForm

    def form_valid(self, form):

        user = form.get_user()
        login(self.request, user)
        url_param = self.request.POST.get('next')
        if url_param:
            return redirect(url_param)
        elif user.is_staff or user.is_superuser:
            return redirect('/index/')
        elif form.data['next'] and "/logout" not in form.data['next'].lower():
            return redirect(form.data['next'])
        else:
            return redirect(reverse_lazy('index'))


class CoreLogoutView(LogoutView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        # Removendo os cookies definidos no login
        response.delete_cookie('user_id')
        response.delete_cookie('username')
        response.delete_cookie('user_email')
        response.delete_cookie('valid')

        return response

class SuccessView(TemplateView):
    template_name = 'success.html'

class CadastroView(FormView):
    template_name = 'auth/cadastro.html'
    form_class = CadastroForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        try:
            with transaction.atomic():
                print(type(form.cleaned_data['password']))
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name']
                )
            messages.success(self.request, "Cadastro realizado com sucesso!")
            return super().form_valid(form)
        except Exception as e:
            print(e)
            messages.error(self.request, "Erro ao realizar cadastro.")
            return self.form_invalid(form)