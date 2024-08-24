from django import template
from urllib.parse import quote_plus

register = template.Library()

@register.filter(name='encode_string')
def encode_string(string):
    return quote_plus(string)