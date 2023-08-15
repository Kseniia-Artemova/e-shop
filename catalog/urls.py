from django.urls import path
# from catalog.views import product, catalog, category, contacts, home, create_product
from catalog.views import ProductsListView, CategoryProductsListView, ContactsView, ProductDeleteView
from catalog.views import HomeView, ProductCreateView, ProductDetailView, ProductUpdateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('', HomeView.as_view(), name='home'),
    # path('contacts/', contacts, name='contacts'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    # path('catalog/', catalog, name='catalog'),
    path('catalog/', ProductsListView.as_view(), name='catalog'),
    # path('<int:pk>/category/', category, name='category'),
    path('<int:pk>/category/', CategoryProductsListView.as_view(), name='category'),
    # path('creation/', create_product, name='creation'),
    path('creation/', ProductCreateView.as_view(), name='creation'),
    # path('<int:pk>/product/', product, name='product'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
]