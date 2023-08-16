from django.urls import path
# from catalog.views import product, catalog, category, contacts, home, create_product
from catalog.views import ProductsListView, CategoryProductsListView, ContactsView, ProductDeleteView
from catalog.views import HomeView, ProductCreateView, ProductDetailView, ProductUpdateView
from catalog.views import BlogEntryListView, BlogEntryCreateView, BlogEntryUnpublishedListView
from catalog.views import BlogEntryDetailView, publish_blog_entry, BlogEntryUpdateView, BlogEntryDeleteView
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
    path('creation_product/', ProductCreateView.as_view(), name='creation_product'),
    # path('<int:pk>/product/', product, name='product'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('<int:pk>/update_product/', ProductUpdateView.as_view(), name='update_product'),
    path('<int:pk>/delete_product/', ProductDeleteView.as_view(), name='delete_product'),
    path('blog/', BlogEntryListView.as_view(), name='blog'),
    path('unpublished_entries/', BlogEntryUnpublishedListView.as_view(), name='unpublished_entries'),
    path('new_entry/', BlogEntryCreateView.as_view(), name='new_entry'),
    path('<int:pk>/entry/', BlogEntryDetailView.as_view(), name='blog_entry'),
    path('activity/<int:pk>/', publish_blog_entry, name='publish'),
    path('<int:pk>/update_entry/', BlogEntryUpdateView.as_view(), name='update_entry'),
    path('<int:pk>/delete_entry/', BlogEntryDeleteView.as_view(), name='delete_entry'),
]