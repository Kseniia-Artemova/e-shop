from django.urls import path
from catalog.views import home, contacts, catalog, category, create_product
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', catalog, name='catalog'),
    path('<int:pk>/category/', category, name='category'),
    path('creation/', create_product, name='creation'),
    path('<int:pk>/product/', category, name='product'),
]