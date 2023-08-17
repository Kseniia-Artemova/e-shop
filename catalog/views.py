import django.core.handlers.wsgi
from django.http.response import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

from django.shortcuts import render, redirect, get_object_or_404
from catalog.services import send_congratulatory_email
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from config.settings import ENTRY_PATH
from catalog.models import Product, Contact, Category, BlogEntry
from pytils.translit import slugify


# Create your views here.
COUNT_LATEST_PRODUCTS = 5


# def home(request: WSGIRequest) -> HttpResponse:
#     """
#     Контроллер для отображения домашней страницы
#     """
#     context = {
#         'product_list': Product.objects.order_by('-change_date')[:5],
#         'category_list': Category.objects.all()
#     }
#     return render(request, 'catalog/home.html', context)


class HomeView(TemplateView):
    """
    Класс-контроллер для отображения домашней страницы
    """
    template_name = 'catalog/home.html'
    extra_context = {
        'product_list': Product.objects.order_by('-change_date')[:COUNT_LATEST_PRODUCTS],
        'category_list': Category.objects.all()
    }


# def contacts(request: WSGIRequest) -> HttpResponse:
#     """
#     Контроллер для отображения страницы с контактами и обратной связью
#     """
#     context = {
#         'contact_data': Contact.objects.get(pk=2),
#     }
#     if request.method == "POST":
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         with open(ENTRY_PATH, "a", encoding="UTF-8") as file:
#             print(f'You have new message from {name}({phone}): {message}', file=file)
#     return render(request, 'catalog/contacts.html', context)


class ContactsView(TemplateView):
    """
    Класс-контроллер для отображения страницы с контактами и обратной связью
    """
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            with open(ENTRY_PATH, "a", encoding="UTF-8") as file:
                print(f'You have new message from {name}({phone}): {message}', file=file)
        context_data['contact_data'] = Contact.objects.get(pk=2)
        return context_data


# def catalog(request: WSGIRequest) -> HttpResponse:
#     """
#     Контроллер для отображения страницы со списком всех товаров
#     """
#     context = {
#         'product_list': Product.objects.all(),
#     }
#     return render(request, 'catalog/catalog.html', context)


class ProductsListView(ListView):
    """
    Класс-контроллер для отображения страницы со списком всех товаров
    в порядке от новых к более старым
    """
    model = Product
    template_name = 'catalog/catalog.html'

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        return queryset.order_by('-change_date')


# def category(request: WSGIRequest, pk: int) -> HttpResponse:
#     """
#     Контроллер для отображения страницы со списком товаров,
#     принадлежащих конкретной категории
#     """
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'product_list': Product.objects.filter(category_id=pk),
#         'title': category_item.name
#     }
#     return render(request, 'catalog/category.html', context)


class CategoryProductsListView(ListView):
    """
    Класс-контроллер для отображения страницы со списком товаров,
    принадлежащих конкретной категории
    """
    model = Product
    template_name = 'catalog/category.html'

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = Category.objects.get(pk=self.kwargs.get('pk'))
        return context_data


# def create_product(request: WSGIRequest) -> HttpResponse:
#     """
#     Контроллер для отображения страницы с карточкой описания нового товара.
#     После отправки этой информации товар будет создан и добавлен в базу данных,
#     если все обязательные поля заполнены
#     """
#     context = {
#         'category_list': Category.objects.order_by('pk'),
#     }
#     if request.method == "POST":
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         category = request.POST.get('category')
#         price = request.POST.get('price')
#         image = request.FILES.get('image', None)
#
#         creation_product = {
#             'name': name,
#             'description': description,
#             'category': Category.objects.get(pk=category),
#             'price': price,
#         }
#         if image:
#             creation_product['image'] = image
#         if all(creation_product.values()):
#             Product.objects.create(**creation_product)
#     return render(request, 'catalog/create_product.html', context)


class ProductCreateView(CreateView):
    """
    Класс-контроллер для отображения страницы с карточкой описания нового товара.
    После отправки этой информации товар будет создан и добавлен в базу данных,
    если все обязательные поля заполнены
    """
    model = Product
    template_name = 'catalog/product_form.html'
    fields = ('name', 'description', 'category', 'price', 'image')
    extra_context = {
        'category_list': Category.objects.order_by('pk'),
        'action': 'Создать'
    }
    success_url = reverse_lazy('catalog:catalog')


# def product(request: WSGIRequest, pk: int) -> HttpResponse:
#     """
#     Контроллер для отображения страницы с описанием конкретного товара
#     """
#     context = {
#         'product': Product.objects.get(pk=pk),
#     }
#     return render(request, 'catalog/product.html', context)


class ProductDetailView(DetailView):
    """
    Класс-контроллер для отображения страницы с описанием конкретного товара
    """
    model = Product
    template_name = 'catalog/product.html'


class ProductUpdateView(UpdateView):
    """
    Класс-контроллер для изменения карточки товара
    """
    model = Product
    template_name = 'catalog/product_form.html'
    fields = ('name', 'description', 'category', 'price', 'image')
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)
        extra_context = {
            'category_list': Category.objects.order_by('pk'),
            'action': 'Изменить',
            'object': Product.objects.get(pk=self.kwargs.get('pk'))
        }
        return context_data | extra_context


class ProductDeleteView(DeleteView):
    """
    Класс-контроллер для удаления товара
    """
    model = Product
    template_name = 'catalog/delete_form.html'
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)
        extra_context = {
            'object': Product.objects.get(pk=self.kwargs.get('pk'))
        }
        return context_data | extra_context


class BlogEntryListView(ListView):
    """
    Класс-контроллер для отображения страницы со списком публикаций блога
    """
    model = BlogEntry
    template_name = 'catalog/blog.html'

    def get_context_data(self, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)
        object_list = BlogEntry.objects.filter(is_published=True)
        object_list = object_list.order_by('-creation_date')
        context_data['object_list'] = object_list
        context_data['button_text'] = 'Разопубликовать'
        return context_data


class BlogEntryCreateView(CreateView):
    """
    Класс-контроллер для отображения формы создания новой публикации блога
    """
    model = BlogEntry
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:blog')
    template_name = 'catalog/form_blog_entry.html'
    extra_context = {
        'action': 'Создать',
    }

    def form_valid(self, form):
        if form.is_valid():
            new_entry = form.save()
            new_entry.slug = slugify(new_entry.title)
            new_entry.save()
        return super().form_valid(form)


class BlogEntryUnpublishedListView(BlogEntryListView):
    """
    Класс-контроллер для отображения страницы со списком неопубликованных записей блога
    """
    model = BlogEntry
    template_name = 'catalog/unpublished_entries.html'

    def get_context_data(self, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)
        object_list = BlogEntry.objects.filter(is_published=False)
        object_list = object_list.order_by('-creation_date')
        context_data['object_list'] = object_list
        context_data['button_text'] = 'Опубликовать'
        return context_data


class BlogEntryDetailView(DetailView):
    """
    Класс-контроллер для отображения страницы с конкретной записью блога
    """
    model = BlogEntry
    template_name = 'catalog/current_blog_entry.html'

    def get_object(self, queryset=None) -> QuerySet:
        self.object = super().get_object(queryset)
        if self.object.is_published:
            self.object.number_views += 1
            self.object.save()
        if self.object.number_views == 100:
            send_congratulatory_email(self.object)
        return self.object


def publish_blog_entry(request, pk):
    """
    Контроллер для изменения статуса публикации
    (is_published: True/False)
    """
    blog_entry = get_object_or_404(BlogEntry, pk=pk)
    redirect_url = 'catalog:blog' if blog_entry.is_published else 'catalog:unpublished_entries'
    blog_entry.is_published = not blog_entry.is_published
    blog_entry.save()

    return redirect(redirect_url)


class BlogEntryUpdateView(UpdateView):
    """
    Класс-контроллер для изменения записи блога
    """
    model = BlogEntry
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:unpublished_entries')
    template_name = 'catalog/form_blog_entry.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        extra_context = {
            'action': 'Сохранить',
            'object': BlogEntry.objects.get(pk=self.kwargs.get('pk'))
        }
        return context_data | extra_context


class BlogEntryDeleteView(DeleteView):
    """
    Класс-контроллер для удаления записи блога
    """
    model = BlogEntry
    template_name = 'catalog/delete_entry.html'
    success_url = reverse_lazy('catalog:unpublished_entries')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        extra_context = {
            'object': BlogEntry.objects.get(pk=self.kwargs.get('pk'))
        }
        return context_data | extra_context