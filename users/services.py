from django.core.mail import send_mail
from config import settings


def send_verification_url(url, email):
    """
    Функция для оправки ссылки для верификации на почту пользователя
    """
    send_mail(
        subject='Ссылка для верификации',
        message=f'Пожалуйста, пройдите по ссылке для верификации вашего аккаунта:\n'
                f'{url}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )