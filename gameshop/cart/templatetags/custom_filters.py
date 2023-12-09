from django import template

register = template.Library()


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key, None)


@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg
