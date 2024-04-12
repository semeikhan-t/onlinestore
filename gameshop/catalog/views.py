import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView

from payment.models import PaymentData
from .forms import ProductReviewForm
from .models import Product, ProductReview
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        product = self.object
        context['form'] = ProductReviewForm(self.request.POST, initial={'user': user, 'product': product.id})
        context['reviews'] = ProductReview.objects.filter(product=product).order_by('-date')
        return context

    def post(self, request, pk):
        form = ProductReviewForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            product = get_object_or_404(Product, id=pk)
            form.instance.product = product
            form.save()
            response = redirect('home')
            return response
        else:
            form.add_error(None, 'Ошибка публикации отзыва!')
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class AddReviewView(View, LoginRequiredMixin):
    login_url = '/login/'

    def post(self, request, slug):
        if request.user.is_authenticated:
            user = request.user
            print(f'User: {user}')
            user_orders = PaymentData.objects.filter(user=user)
            user_ordered = False
            for order in user_orders:
                slugs_from_json = list(json.loads(order.cart).keys())
                if slug in slugs_from_json:
                    user_ordered = True
                    break
            print(f'User ordered: {user_ordered}')

            product = get_object_or_404(Product, slug=slug)

            product_reviews = ProductReview.objects.filter(product=product)
            user_reviewed = False
            for review in product_reviews:
                print(f'Review: {review}')
                if str(user) is str(review.user):
                    user_reviewed = True
                    break
            print(f'User reviewed: {user_reviewed}')

            if user_ordered and user_reviewed is True:
                form = ProductReviewForm(request.POST, initial={'user': user, 'product': product})
                if form.is_valid():
                    form.instance.product = product
                    form.save()
                    return redirect('catalog-detail', slug=slug)
            else:
                return redirect('catalog-detail', slug=slug)
        else:
            return redirect(self.login_url)

    def get(self, request):
        raise Http404()


class AddToCartView(View):
    def get(self, request):
        raise Http404()

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
