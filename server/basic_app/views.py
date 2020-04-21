from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Product


def basic_view(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:5]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'basic_app/basic_view.html', context)


def second_view(request):
    return HttpResponse("This is second view")


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'basic_app/detail.html', {'product': product})


def results(request, product_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % product_id)


def vote(request, product_id):
    return HttpResponse("You're voting on question %s." % product_id)