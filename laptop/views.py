from django.shortcuts import render, get_object_or_404
from .filter import LaptopFilter
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def catalog(request):
#     catalog = models.Category.objects.all()

#     context = {
#         'catalog':catalog,
#     }
#     return render(request, 'base.html', context)


def prodact(request):
    l = models.Laptop.objects.all()     #Laptop List

    lf = LaptopFilter(request.GET, queryset=l)     #Laptop Filter
    pro = LaptopFilter(request.GET, queryset=l).qs 
    # catalog = models.Category.objects.all() 
    paginator = Paginator(pro, 10)
    page = request.GET.get('page')

    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    context = {
        # 'catalog':catalog,        
        'laptops':l,
        'filter':lf,
        'product':product,
    }
    return render(request, 'product.html',context)

def product_detail(request, pk, slug):
    pro_detail = get_object_or_404(models.Laptop,pk=pk, slug=slug)
    context = {
        'pro_detail':pro_detail,
    }
    return render(request, 'product-details.html', context)

