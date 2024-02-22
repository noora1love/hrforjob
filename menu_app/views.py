from django.shortcuts import render
from .models import MenuItem

def home(request):
    main_menu = MenuItem.objects.select_related('parent').all()
    return render(request, 'home.html', {'main_menu': main_menu})



def about(request):
    # Загружаем все элементы меню и их дочерние элементы
    main_menu = MenuItem.objects.select_related('parent').all()
    return render(request, 'about.html', {'main_menu': main_menu})


def get_main_menu():
    return MenuItem.objects.filter(parent__isnull=True)

def get_menu_by_name(menu_name):
    return MenuItem.objects.filter(title=menu_name, parent__isnull=True)
