import json
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Product, ProductCategory
from .utils import DataMixin


class CatalogView(DataMixin, ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'items'
    extra_context = {'title': 'Каталог'}

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return Product.objects.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )
        else:
            return Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        search_query = self.request.GET.get('search', None)
        if not self.object_list.exists() and search_query:
            context['no_results'] = f'По запросу "{search_query}" к сожалению ничего не найдено :('
        return dict(list(c_def.items()) + list(context.items()))


class CatalogDetailView(DetailView):
    model = Product
    template_name = "catalog/details_view.html"
    context_object_name = "item_card"


class AddToCartView(View):
    def post(self, request, slug):
        if request.method == 'POST':
            quantity = request.POST.get('quantity', 1)
            cart = request.COOKIES.get('cart', '{}')
            cart = json.loads(cart)

            current_quantity = cart.get(slug, 0)
            cart[slug] = current_quantity + int(quantity)

            response = redirect('catalog')
            response.set_cookie('cart', json.dumps(cart))
            return response

    def get(self, request):
        raise Http404()


class ShowCategory(DataMixin, ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'items'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ', cat_selected=self.kwargs['slug'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_category(request, slug):
#     items = Product.objects.filter(cat__slug=slug)
#     category = ProductCategory.objects.all()
#
#     context = {
#         'items': items,
#         'cat_selected': slug,
#         'title': 'Отображение по категориям',
#         'cats': category,
#     }
#
#     return render(request, 'catalog/catalog.html', context=context)
