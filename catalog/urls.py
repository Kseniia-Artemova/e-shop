from django.urls import path
from catalog.views import get_home, take_contacts


urlpatterns = [
    path('', get_home),
    path('contacts/', take_contacts)
]