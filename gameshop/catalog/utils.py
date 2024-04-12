from django.db.models import Count
from .models import *


class DataMixin:
    paginate_by = 9

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = ProductCategory.objects.annotate(Count('product'))
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
            context['title'] = 'Каталог'
        else:
            for i in cats:
                if i.slug == context['cat_selected']:
                    context['title'] = f'Категория - {i.name}'
        return context
