import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from payment.forms import PaymentForm
from catalog.models import Product


class PaymentView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'payment/payment.html'

    def get(self, request, *args, **kwargs):
        cart = request.COOKIES.get('cart', '{}')
        cart = json.loads(cart)

        product_slugs = list(cart.keys())
        products = Product.objects.filter(slug__in=product_slugs)

        total_price = sum(product.price * cart[product.slug] for product in products)
        cart_value_from_cookie = request.COOKIES.get('cart', None)
        user = request.user

        form = PaymentForm(
            initial={'cart_from_cookie': cart_value_from_cookie, 'total_price': total_price, 'user': user}
        )
        context = {'form': form, 'products': products, 'cart': cart, 'total_price': total_price}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        cart_value_from_cookie = request.COOKIES.get('cart', None)
        cart = json.loads(cart_value_from_cookie)

        product_slugs = list(cart.keys())
        products = Product.objects.filter(slug__in=product_slugs)

        total_price = sum(product.price * cart[product.slug] for product in products)
        user = request.user

        form = PaymentForm(request.POST,
                           initial={'cart_from_cookie': cart_value_from_cookie, 'total_price': total_price, 'user': user})

        if form.is_valid():
            try:
                form.save()
                response = redirect('home')
                response.delete_cookie('cart')
                return response
            except:
                form.add_error(None, 'Ошибка оплаты')

        context = {'form': form, 'products': products, 'cart': cart, 'total_price': total_price}
        return render(request, self.template_name, context=context)
