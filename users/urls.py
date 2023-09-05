from django.contrib.auth.views import LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, LoginView, verification, VerifyMessage, UserUpdateView, generate_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),
    path('verify_message/', VerifyMessage.as_view(), name='verify_message'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/genpassword/', generate_new_password, name='new_password'),
    path('verification/<str:verification_code>', verification, name='verification'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
]