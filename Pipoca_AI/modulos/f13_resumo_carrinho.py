def exibir_resumo_pedido(banco_dados, id_pedido):
    # PASSO 1 da ficha: o pedido existe?
    if id_pedido not in banco_dados["assinaturas_transacoes"]:
        print("Pedido nao encontrado!")
        return

    # Pegar a "caixinha" do pedido
    pedido = banco_dados["assinaturas_transacoes"][id_pedido]

    # PASSO 2 da ficha: cabecalho
    print("=" * 45)
    print(f"Pedido: {id_pedido}")
    print(f"Usuario: @{pedido['nickname']}")
    print(f"Email: {pedido['email_usuario']}")
    print(f"Assinante anual: {pedido['assinante_anual']}")
    print(f"Status: {pedido['status']}")
    print(f"Pagamento: {pedido['metodo_pagamento']}")

    # PASSO 3 da ficha: itens do carrinho
    print("-" * 45)
    print("Itens do carrinho:")
    for item in pedido["carrinho"]:
        print(f"{item['categoria']} | {item['descricao']} | Qtd: {item['qtd']} | R$ {item['subtotal']:.2f}")

    # PASSO 4 da ficha: rodape
    print("-" * 45)
    print(f"Valor bruto:    R$ {pedido['valor_bruto']:.2f}")
    print(f"Valor desconto: R$ {pedido['valor_desconto']:.2f}")
    print(f"Valor liquido:  R$ {pedido['valor_liquido']:.2f}")
