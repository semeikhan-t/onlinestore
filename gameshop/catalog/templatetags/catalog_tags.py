import json
from django import template
from catalog.models import *
from payment.models import PaymentData

register = template.Library()


@register.inclusion_tag('catalog/catalog.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = ProductCategory.objects.all()
    else:
        cats = ProductCategory.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.simple_tag
def can_review(user, product_slug):
    user_orders = PaymentData.objects.filter(user=user)
    user_ordered = False
    for order in user_orders:
        slugs_from_json = list(json.loads(order.cart).keys())
        if product_slug in slugs_from_json:
            user_ordered = True
            break

    if not user_ordered:
        return False

    product_reviews = ProductReview.objects.filter(product__slug=product_slug)
    user_reviewed = any(str(review.user) == str(user) for review in product_reviews)
    return not user_reviewed
