from django.template import Library

register = Library()

@register.filter
def formata_preco(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')