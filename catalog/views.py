from django.shortcuts import render
from config.settings import ENTRY_PATH
from catalog.models import Product, Contact, Category

# Create your views here.
COUNT_LATEST_PRODUCTS = 5


def home(request):
    context = {
        'product_list': Product.objects.order_by('change_date')[:5],
        'category_list': Category.objects.all()
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'contact_data': Contact.objects.get(pk=2),
    }
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open(ENTRY_PATH, "a", encoding="UTF-8") as file:
            print(f'You have new message from {name}({phone}): {message}', file=file)
    return render(request, 'catalog/contacts.html', context)


def catalog(request):
    context = {
        'product_list': Product.objects.all(),
    }
    return render(request, 'catalog/catalog.html', context)


def category(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'product_list': Product.objects.filter(category_id=pk),
        'title': category_item.name
    }
    return render(request, 'catalog/category.html', context)