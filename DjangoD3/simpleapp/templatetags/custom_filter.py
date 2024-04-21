# register = template.Library()
#
#
# # Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# # что это именно фильтр для шаблонов, а не простая функция.
# @register.filter()
# def currency(value):
#    """
#    value: значение, к которому нужно применить фильтр
#    """
#    # Возвращаемое функцией значение подставится в шаблон.
#    return f'{value} Р'
from datetime import datetime

from django import template
# from datetime import datetime

register = template.Library()

CURRENCIES_SYMBOLS = {
    'rub': 'Р',
    'usd': '$',
    'eur': '€',
}


@register.filter()
def currency(value, code='rub'):
    """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
    postfix = CURRENCIES_SYMBOLS[code]

    return f'{value} {postfix}'



