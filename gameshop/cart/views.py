import json
from django.shortcuts import render, redirect
from catalog.models import Product
from django.views import View


class CartView(View):
    template_name = 'cart/view_cart.html'

    def get(self, request):
        cart = request.COOKIES.get('cart', '{}')
        cart = json.loads(cart)

        product_slugs = list(cart.keys())
        products = Product.objects.filter(slug__in=product_slugs)

        total_price = sum(product.price * cart[product.slug] for product in products)

        context = {'products': products, 'cart': cart, 'total_price': total_price}
        return render(request, self.template_name, context=context)


class RemoveFromCartView(View):
    def get(self, request, slug, *args, **kwargs):
        cart = request.COOKIES.get('cart', '{}')
        cart = json.loads(cart)
        response = redirect("view_cart")

        if slug in cart:
            del cart[slug]
            response.set_cookie('cart', json.dumps(cart))
        return response
