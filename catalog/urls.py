from django.urls import path
from catalog.views import home, contacts, catalog


urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('catalog/', catalog),
]