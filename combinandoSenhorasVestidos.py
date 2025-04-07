# 3 senhoras com vestidos
# nomes: branca, violeta e rosa
# cores : branca, violeta e rosa
# nomes != cores => print nome e cores

from itertools import permutations

def normalizar_palavras(palavra):
    if palavra.lower().endswith(('o','a')):
        return palavra.lower()[:-1]
    return palavra.lower()


nomes = ['Branca','Violeta','Rosa']
vestidos = ['branco','violeta','rosa']

#gera todas as permutaçoes possiveis dos vestidos
combinacoes_possiveis = list(permutations(vestidos))

print (f"Combinações possiveis onde cada senhora usa um vestido de cor diferente de seu nome:\n")
print ("Combinaçoes validas:\n")


for vestidos_combinacao in combinacoes_possiveis:
    #criar pares de combinaçoes de (nome, vestido) para cada combinaçao possivel
    pares = list(zip(nomes, vestidos_combinacao))

    if all (normalizar_palavras(nome) != normalizar_palavras(vestido)  for nome, vestido in pares):
        for nome, vestido in pares:
            print(f"A senhora {nome} usa vestido {vestido}")
        print()
            