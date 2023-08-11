from django.shortcuts import render
from config.settings import ENTRY_PATH
from catalog.models import Product, Contact

# Create your views here.
COUNT_LATEST_PRODUCTS = 5


def home(request):
    # TODO: поиграть со стилями и разметкой
    context = {
        'object_list': Product.objects.order_by('change_date')[:5]
    }
    return render(request, 'catalog/index_2.html', context)


def contacts(request):
    # TODO: поиграть со стилями и разметкой
    contact_data = Contact.objects.get(pk=2)
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open(ENTRY_PATH, "a", encoding="UTF-8") as file:
            print(f'You have new message from {name}({phone}): {message}', file=file)
    return render(request, 'catalog/contacts.html', {'contact_data': contact_data})


def catalog(request):
    # TODO: тут добавить нормальную страницу
    context = {
        'object_list': Product.objects.order_by('change_date')[:5]
    }
    return render(request, 'catalog/catalog.html', context)
