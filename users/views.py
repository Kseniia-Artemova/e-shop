from django.contrib.auth.views import LoginView as BaseLoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from users.forms import UserForm, LoginForm
from users.models import User
import secrets
import users.services as services


class RegisterView(CreateView):
    """Класс-контроллер для регистрации нового пользователя"""

    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:verify_message')
    template_name = 'users/registration.html'

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            verification_code = secrets.token_urlsafe(nbytes=7)
            instance.verification_code = verification_code

            url = reverse('users:verification', args=[verification_code])
            total_url = self.request.build_absolute_uri(url)
            services.send_verification_url(total_url, instance.email)

            instance.save()
        return super().form_valid(form)


class LoginView(BaseLoginView):
    """Класс-контроллер для реализации авторизации пользователя"""

    template_name = 'users/login.html'
    form_class = LoginForm


class VerifyMessage(TemplateView):
    template_name = 'users/verification_message.html'


def verification(request, verification_code):
    user = User.objects.get(verification_code=verification_code)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))