import json
from django.http import Http404
from django.shortcuts import render, redirect
from catalog.models import Product


def view_cart(request):
    cart = request.COOKIES.get('cart', '{}')
    cart = json.loads(cart)

    product_slugs = list(cart.keys())
    products = Product.objects.filter(slug__in=product_slugs)

    total_price = sum(product.price * cart[product.slug] for product in products)

    context = {'products': products, 'cart': cart, 'total_price': total_price}
    return render(request, 'cart/view_cart.html', context=context)


# def view_cart(request):
#     cart = request.COOKIES.get('cart', '')
#     all_cart_items = json.loads(cart) if cart else {}
#
#     # Получаем список товаров по их ID из корзины
#     product_ids = list(map(int, all_cart_items.keys()))
#     products = Product.objects.filter(id__in=product_ids)
#
#     # Вычисляем общую стоимость товаров в корзине
#     total_price = sum(
#         products_dict['price'] * all_cart_items[str(products_dict['id'])] for products_dict in products.values())
#
#     return render(
#         request, 'cart/view_cart.html', {'products': products, 'total_price': total_price}
#     )


def remove_from_cart(request, slug):
    cart = request.COOKIES.get('cart', '{}')
    cart = json.loads(cart)

    if slug in cart:
        del cart[slug]
        response = redirect("http://127.0.0.1:8000/view_cart/")
        response.set_cookie('cart', json.dumps(cart))
        return response
    else:
        return redirect("http://127.0.0.1:8000/view_cart/")
