from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products


def catalog(request, cat_slug):
    
    page = request.GET.get('page', 1)
    
    if cat_slug == 'all':
        goods = Products.objects.all()
        
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=cat_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
    
    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": cat_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)
    
    context = {
        "product": product,
    }
    
    return render(request, "goods/product.html", context=context)
