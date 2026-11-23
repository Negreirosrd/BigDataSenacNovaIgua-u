from banco_dados import banco_dados
from modulos.f13_resumo_carrinho import exibir_resumo_pedido

# O banco veio com assinaturas_transacoes VAZIO.
# Entao criamos 2 pedidos de teste, escritos a mao, para o F13 ter o que mostrar.
banco_dados["assinaturas_transacoes"][2026001] = {
    "email_usuario": "ana@email.com",
    "nickname": "ana_pipoca",
    "assinante_anual": True,
    "carrinho": [
        {"categoria": "STREAMING", "descricao": "Plano Sofa Compartilhado (4K + IA)", "qtd": 12, "subtotal": 560.0},
        {"categoria": "LIVE_PPV", "descricao": "Final Mundial Valorant 2026 (POV Pro)", "qtd": 2, "subtotal": 79.8},
    ],
    "valor_bruto": 639.8,
    "valor_desconto": 63.98,
    "valor_liquido": 575.82,
    "metodo_pagamento": "PIX",
    "status": "PAGO",
}
banco_dados["assinaturas_transacoes"][2026002] = {
    "email_usuario": "beto@email.com",
    "nickname": "beto_cinema",
    "assinante_anual": False,
    "carrinho": [],
    "valor_bruto": 0.0,
    "valor_desconto": 0.0,
    "valor_liquido": 0.0,
    "metodo_pagamento": "PENDENTE",
    "status": "ABERTO",
}

# Mostra o extrato de TODOS os pedidos que existem
for id_pedido in banco_dados["assinaturas_transacoes"]:
    exibir_resumo_pedido(banco_dados, id_pedido)
    print()

# Pedido que NAO existe
exibir_resumo_pedido(banco_dados, 9999999)
