from django.shortcuts import render
from config.settings import ENTRY_PATH

# Create your views here.


def home(request):
    return render(request, 'catalog/homepage.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open(ENTRY_PATH, "a", encoding="UTF-8") as file:
            print(f'You have new message from {name}({phone}): {message}', file=file)
    return render(request, 'catalog/contact_page.html')
