from django.template import Library
from utils import utils

register = Library()

@register.filter
def formata_preco(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')

@register.filter
def total_carrinho(carrinho):
    return utils.total_carrinho(carrinho)

@register.filter
def cart_total(carrinho):
    return utils.cart_total(carrinho)