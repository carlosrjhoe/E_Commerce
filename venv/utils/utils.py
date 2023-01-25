def total_carrinho(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])