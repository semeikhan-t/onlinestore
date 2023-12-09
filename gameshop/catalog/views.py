import json
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Product


def catalog(request):
    global items
    search_query = request.GET.get('search', None)
    if search_query:
        items = Product.objects.filter(
            Q(title__icontains=search_query)
            |
            Q(description__icontains=search_query)
        )
    else:
        items = Product.objects.all()
    context = {'items': items}
    if not items.exists() and search_query:
        context['no_results'] = f'По запросу "{search_query}" к сожалению ничего не найдено :('
    return render(request, 'catalog/catalog.html', context)


class CatalogDetailView(DetailView):
    model = Product
    template_name = "catalog/details_view.html"
    context_object_name = "item_card"


def add_to_cart(request, slug):
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        cart = request.COOKIES.get('cart', '{}')
        cart = json.loads(cart)

        current_quantity = cart.get(slug, 0)
        cart[slug] = current_quantity + int(quantity)

        response = redirect('http://127.0.0.1:8000/catalog/')
        response.set_cookie('cart', json.dumps(cart))
        return response

    # Вернуть ошибку или выполнить другие действия в случае GET-запроса
    return HttpResponse("Invalid request method")

# def add_to_cart(request, slug, quantity):
#     try:
#         item = Product.objects.get(slug=slug)
#
#         # Проверяем, есть ли куки 'cart'
#         cart_cookie = request.COOKIES.get('cart', '')
#
#         # Преобразуем содержимое 'cart' из строки JSON в словарь
#         cart_dict = json.loads(cart_cookie) if cart_cookie else {}
#
#         # Увеличиваем количество товара в корзине
#         cart_dict[str(item.id)] = cart_dict.get(str(item.id), 0) + quantity
#
#         # Преобразуем словарь обратно в строку JSON
#         cart_cookie_updated = json.dumps(cart_dict)
#
#         # Создаем HTTP-ответ и устанавливаем обновленную корзину в куки
#         response = redirect('http://127.0.0.1:8000/catalog/')
#         response.set_cookie('cart', cart_cookie_updated)
#         print(f"Cart Cookie Contents: {cart_cookie_updated}")
#         return response
#
#     except Product.DoesNotExist:
#         raise Http404("Product does not exist")
#     except Exception as e:
#         # Обработка других исключений (например, JSONDecodeError)
#         print(e)
#         raise Http404
