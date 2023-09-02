from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


class UserForm(UserCreationForm):
    """ Форма для регистрации пользователя """

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].help_text = None

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'text-align: center;'

class LoginForm(AuthenticationForm):
    """ Форма для аутентификации пользователя """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'text-align: center;'

