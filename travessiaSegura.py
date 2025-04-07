# um homem com um barco que aguenta ele e mais uma carga
# cargas = lobo, um bode e um maço de alfafa

# #lobo come o bode
# #bode come o maço de alfafa

def verificar_estado_seguro(lado):
    """Verifica se um  lado é seguro, sem o lobo comendo o bode ou o bode comendo a alfafa"""
    if "homem" not in lado: # se homem nao esta presente
        if "lobo" in lado and "bode" in lado:
            print("O lobo vai comer o bode")
            return False #lobo come o bode
        if "bode" in lado and "maço de alfafa" in lado:
            print("O bode vai comer a alfafa")
            return False #bode como alfafa
    return True

def adicionar_itens (lista,itens):
    """Adiciona itens de uma lista e retorna lista atualizada"""
    for item in itens:
        if item not in lista:
            lista.append(item)
    return lista

def remover_itens(lista,itens):
    """Remover itens de umma lista e retorna nova lista atualizada"""
    return [ x for x in lista if x not in itens]

def preparar_bote (lado_origem, passageiro=None):
    """Preparar bote colocando homem e opcionalmente um passageiro"""
    bote = []
    if "homem" in lado_origem:
        lado_origem.remove("homem")
        bote.append("homem")
        if passageiro and passageiro in lado_origem:
            lado_origem.remove(passageiro)
            bote.append(passageiro)
    return  bote

def fazer_travessia():
  
    #estado inicial
    lado_inicial = ["homem", "lobo", "maço de alfafa","bode"]
    lado_final=[]

    print (f"Estado inicial:  {lado_inicial} | {lado_final}")

    #primeira travessia, levar o bode
    bote = preparar_bote(lado_inicial,"bode")
    print(f"Bote atravessando com: {bote}")
    lado_final = adicionar_itens(lado_final,bote)

    if not verificar_estado_seguro (lado_inicial):
        print("ERROR: Estado inseguro detectado!")
        return
    print (f"Estado atual: {lado_inicial} | {lado_final}")

    #Volta 1: homem retorna sozinho
    bote = preparar_bote(lado_final)
    print(f"Bote retornando com: {bote}")
    lado_inicial= adicionar_itens(lado_inicial,bote)
    lado_final = remover_itens(lado_final,bote)

    if not verificar_estado_seguro (lado_final):
        print("ERROR: Estado inseguro detectado!")
        return
    print (f"Estado atual: {lado_inicial} | {lado_final}")

    #Segunda travessia, levar o maço de alfafa
    bote = preparar_bote(lado_inicial,"maço de alfafa")
    print(f"Bote atravessando com: {bote}")
    lado_final = adicionar_itens(lado_final,bote)

    #levar o bode de volta
    bote = preparar_bote(lado_final,"bode")
    print(f"Bote atravessando com: {bote}")
    lado_inicial= adicionar_itens(lado_inicial,bote)

    if not verificar_estado_seguro (lado_final):
        print("ERROR: Estado inseguro detectado!")
        return
    print (f"Estado atual: {lado_inicial} | {lado_final}")

    #lavar o lobo
    bote = preparar_bote(lado_inicial,"lobo")
    print(f"Bote atravessando com: {bote}")
    lado_final = adicionar_itens(lado_final,bote)

    if not verificar_estado_seguro (lado_final):
        print("ERROR: Estado inseguro detectado!")
        return
    print (f"Estado atual: {lado_inicial} | {lado_final}")

    #homem retorna sozinho
    bote = preparar_bote(lado_final)
    print(f"Bote retornando com: {bote}")
    lado_inicial= adicionar_itens(lado_inicial,bote)
    lado_final = remover_itens(lado_final,bote)

    #lavar o bode
    bote = preparar_bote(lado_inicial,"bode")
    print(f"Bote atravessando com: {bote}")
    lado_final = adicionar_itens(lado_final,bote)

    
    if not verificar_estado_seguro (lado_final):
        print("ERROR: Estado inseguro detectado!")
        return
    print (f"Estado atual: {lado_inicial} | {lado_final}")
    

if __name__ == "__main__":
    fazer_travessia()

