from django import template
from catalog.models import *

register = template.Library()


@register.inclusion_tag('catalog/catalog.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = ProductCategory.objects.all()
    else:
        cats = ProductCategory.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}
