#Atividade 2:

'''O objetivo é, dadas as 4 notas de um estudante, calcular sua média e,
com base nela, emitir a mensagem de status correspondente: 
1. Aprovado: Média estritamente maior que 7;
2. Recuperação: Média entre 5 (inclusive) e 7 (inclusive);
3. Reprovação: Média estritamente abaixo de 5.'''

#Comando inicial
print("Bem-vindo à Calculadora de Nota!")

nota_1 = int(input("Insira sua primeira nota:"))
nota_2 = int(input("Insira sua segunda nota:"))
nota_3 = int(input("Insira sua terceira nota:"))
nota_4 = int(input("Insira sua quarta nota:"))

#Aprovado: Média estritamente maior que 7. 
#Recuperação: Média entre 5 (inclusive) e 7 (inclusive).
#Reprovação: Média estritamente abaixo de 5.

media = nota_1 + nota_2 + nota_3 + nota_4
total = media / 4
print("Sua média é:", total)

if total <= 5:
    print("Reprovado")
elif total >= 7:
    print("Aprovado")
elif total > 5 and total < 7:
    print("Em Recuperação")
    