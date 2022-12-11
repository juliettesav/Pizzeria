from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request): 
    return render(request, 'pizzas/index.html')

def menu(request):
    menu = Pizza.objects.all()

    context = {'all_menu':menu}
    
    return render(request, 'pizzas/menu.html', context)

def item(request, item_id):
    p = Pizza.objects.get(id=item_id)
    
    entries = Entry.objects.filter(item=p)

    context = {'item':p, 'entries':entries}
    
    return render(request, 'pizzas/item.html', context)
    