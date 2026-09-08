from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):

    premium_mattresses = Product.objects.filter(
        category='mattress',
        collection='premium',
        is_available=True
    )

    standard_mattresses = Product.objects.filter(
        category='mattress',
        collection='standard',
        is_available=True
    )

    products = Product.objects.filter(
        is_available=True
    )

    context = {
        'premium_mattresses': premium_mattresses,
        'standard_mattresses': standard_mattresses,
        'products': products,
    }

    return render(
        request,
        'home.html',
        context
    )
def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
        is_available=True
    )

    return render(
        request,
        'product_detail.html',
        {
            'product': product
        }
    )