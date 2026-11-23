from banco_dados import banco_dados
from modulos.f15_calculo_cashback_desconto import aplicar_descontos_digitais

# O banco veio com assinaturas_transacoes VAZIO.
# Criamos 2 pedidos de teste a mao, com valor_bruto preenchido.
banco_dados["assinaturas_transacoes"][2026001] = {
    "email_usuario": "ana@email.com",
    "nickname": "ana_pipoca",
    "assinante_anual": True,
    "carrinho": [
        {"categoria": "STREAMING", "descricao": "Plano Sofa Compartilhado (4K + IA)", "qtd": 12, "subtotal": 560.0},
        {"categoria": "LIVE_PPV", "descricao": "Final Mundial Valorant 2026 (POV Pro)", "qtd": 2, "subtotal": 79.8},
    ],
    "valor_bruto": 639.8,
    "valor_desconto": 0.0,
    "valor_liquido": 639.8,
    "metodo_pagamento": "PENDENTE",
    "status": "ABERTO",
}
banco_dados["assinaturas_transacoes"][2026002] = {
    "email_usuario": "beto@email.com",
    "nickname": "beto_cinema",
    "assinante_anual": False,
    "carrinho": [
        {"categoria": "LOJA_DIGITAL", "descricao": "Passe de Batalha: Temporada Cyber 2026", "qtd": 2, "subtotal": 89.8},
    ],
    "valor_bruto": 89.8,
    "valor_desconto": 0.0,
    "valor_liquido": 89.8,
    "metodo_pagamento": "PENDENTE",
    "status": "ABERTO",
}

# Pedido 2026001 (assinante anual): sem cupom e com cupom
print("2026001 sem cupom:", aplicar_descontos_digitais(banco_dados, 2026001, False))
print("2026001 com cupom:", aplicar_descontos_digitais(banco_dados, 2026001, True))

# Pedido 2026002 (NAO anual): sem cupom e com cupom
print("2026002 sem cupom:", aplicar_descontos_digitais(banco_dados, 2026002, False))
print("2026002 com cupom:", aplicar_descontos_digitais(banco_dados, 2026002, True))

# O que ficou escrito na sacolinha do 2026001
pedido = banco_dados["assinaturas_transacoes"][2026001]
print("Valor bruto:    R$", pedido["valor_bruto"])
print("Valor desconto: R$", pedido["valor_desconto"])
print("Valor liquido:  R$", pedido["valor_liquido"])
