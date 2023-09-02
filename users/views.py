from django.contrib.auth.views import LoginView as BaseLoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserForm, LoginForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'users/registration.html'


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
