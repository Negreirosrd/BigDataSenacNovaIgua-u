def aplicar_descontos_digitais(banco_dados, id_pedido, cupom_influencer_valido):
    # Passo 1: pegar a sacolinha (o pedido)
    pedido = banco_dados["assinaturas_transacoes"][id_pedido]

    # Passo 2: a cesta de desconto comeca vazia
    percentual = 0.0

    # Passo 3: assinante anual ganha 10%
    if pedido["assinante_anual"] == True:
        percentual += 0.10

    # Passo 4: cupom de influencer ganha mais 10%
    if cupom_influencer_valido == True:
        percentual += 0.10

    # Passo 5: as contas
    valor_desconto = round(pedido["valor_bruto"] * percentual, 2)
    valor_liquido = round(pedido["valor_bruto"] - valor_desconto, 2)

    # Passo 6: escrever na sacolinha e devolver o valor final
    pedido["valor_desconto"] = valor_desconto
    pedido["valor_liquido"] = valor_liquido
    return valor_liquido
