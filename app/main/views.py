from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "url": True,
        
    }
    return render(request, "main/index.html", context)

def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Iusto molestias magnam ex, praesentium obcaecati ab.",
        
    }
    return render(request, "main/about.html", context)
