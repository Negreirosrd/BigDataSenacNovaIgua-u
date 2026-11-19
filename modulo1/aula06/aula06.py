
## LISTAS:

#indices    0        1        2       3         4
compras = ["arroz", "sabão", "pão", "açúcar", "feijão"]
#print(compras)
#print(compras[-1])

compras2 = [
            "amaciante", "papel toalha", "farinha", "maçã", "pão de forma"
        ]

#print(len(compras2))
#print(compras2[0:8:3])


compras_final = compras + compras2
#print(compras_final)


compras3 = [
            "laranja", 
            "maçã",
            "hamburguer",
            "sal"
        ]

compras_final += compras3
#print(compras_final)




compras_final += ["café"]
#compras_final.append("café")

compras_final.insert(2, "café")
#print(compras_final)

#compras_final.pop(3)
#print(compras_final)

#compras_final.pop()
#print(compras_final)


for i in compras_final:
    print(i)

compras_dezembro=compras_final.copy()
print(compras_dezembro)

compras_final.count("maçã")
#print(compras_final)

compras_final.clear()

#print(compras_final)
#print(compras_dezembro)



## TUPLAS:
#tupla_compras = tuple(compras_dezembro)
#print(tupla_compras)

#tupla_compras ("leite")
#finsl_tupla = tupla_compras

#print(tupla_compras)


#filmes_final_semana = {
#   "O menino e A Garça"
#    "As Branquelas"
#    "Premonição"
#    "Avangers"
#    "Diário de Uma Paixão"
#}

#for i in filmes_final_semana:
    #print(i)
 #   print(i)
                        
             ### DICIONARIO ##

#filmes = {
    #"Titanic": 1997,
    #"Como Treinar Seu Deagão": 2010,
    #"Shrek": 2001,
    #"Star Wars IV": 1984,
    # }


#print(filmes["Titanic"][1])

nomes_filmes = ["Titanic", "Shrek"]
ano_lancamento_filme = [1997,2001]
genero_filmes = ["Drama/Romance", "Comédia/Animação"]
indicacoes_oscar = ["Sim" "Sim"]

titanic_info = ["Titanic", 1997, "Drama/Romance", "Sim"]



