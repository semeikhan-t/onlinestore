import json
from django.shortcuts import render, redirect
from payment.forms import PaymentForm

from catalog.models import Product


def payment(request):
    cart = request.COOKIES.get('cart', '{}')
    cart = json.loads(cart)

    product_slugs = list(cart.keys())
    products = Product.objects.filter(slug__in=product_slugs)

    total_price = sum(product.price * cart[product.slug] for product in products)
    cart_value_from_cookie = request.COOKIES.get('cart', None)

    if request.method == 'POST':
        form = PaymentForm(request.POST, initial={'cart_from_cookie': cart_value_from_cookie, 'total_price': total_price})
        if form.is_valid():
            try:
                form.save()
                response = redirect('home')
                response.delete_cookie('cart')
                return response
            except:
                form.add_error(None, 'Ошибка оплаты')
    else:
        form = PaymentForm
    context = {'form': form, 'products': products, 'cart': cart, 'total_price': total_price}
    return render(request, 'payment/payment.html', context=context)
