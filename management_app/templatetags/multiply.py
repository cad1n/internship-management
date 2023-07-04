from django import template

register = template.Library()


@register.simple_tag()
def multiply(qty, unit_price):
    return "R$" + str(qty * unit_price)
