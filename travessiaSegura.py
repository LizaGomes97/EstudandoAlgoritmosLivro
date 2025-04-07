# um homem com um barco que aguenta ele e mais uma carga
# cargas = lobo, um bode e um maço de alfafa

# #lobo come o bode
# #bode come o maço de alfafa

#PSEUDOCODIGO


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

def mostrar_estado(lado_origem, lado_destino):
    """Mostrar o estado atual dos lados"""
    print(f"Estado atual: \n Lado de Origem: {lado_origem} | Lado de Destino: {lado_destino}")

def fazer_travessia_interativa():
    """Executa a travessia de forma interativa"""
    #estado inicial
    lado_inicial = ["homem","lobo","maço de alfafa", "bode"]
    lado_final=[]

    mostrar_estado(lado_inicial,lado_final)

    while True:
        #verifica se ja concluiu o desafio
        if len(lado_inicial) == 0 and "homem" in lado_final and "lobo" in lado_final and "maço de alfafa" in lado_final and "bode" in lado_final :
            print ("Parabens! Voce completou a travessia com sucesso!")
            break

        #verificar se há situaçoes inseguras
        situacao_insegura_inicial = not verificar_estado_seguro(lado_inicial)
        situacao_insegura_final = not verificar_estado_seguro(lado_final)

        if situacao_insegura_inicial or situacao_insegura_final:
            print("ATENÇAO: Situaçao insegura detectada")
            print("Deseja continuar mesmo assim? (s/n)")
            resposta = input().lower()
            if resposta != 's':
                print("Travessia falhou! Tente novamente")
                break
            else:
                print("Continuando...")

        print("\nEscolha uma ação:")
        print("1 - Levar passageiro do lado inicial para o lado final")
        print("2 - Levar passageiro do lado final para o lado inicial")
        print("3 - Voltar sozinho para o lado inicial")
        print("4 - Voltar sozinho para o lado final")
        print("5 - Sair")

        escolha=input("Sua escolha:  ")

        if escolha =="1":
            if "homem" not in lado_inicial:
                print("O homem nao esta no lado inicial!")
                continue

            print("Escolha um passageiro:")
            for i, item in enumerate(lado_inicial):
                if item != "homem":
                    print(f"{i} - {item}")
            print("ou pressione Enter para ir sozinho")

            escolha_passageiro = input()
            if escolha_passageiro =="":
                passageiro = None
            else:
                try:
                    indice = int(escolha_passageiro)
                    passageiro = lado_inicial[indice]
                    if passageiro == "homem":
                        print ("Homem é quem dirige o barco! Escolha outro passageiro")
                        continue
                except (ValueError, IndexError):
                    print("Escolha invalida!")
                    continue

            bote = preparar_bote(lado_inicial,passageiro)
            print(f"Bote atravessando com: {bote}")
            lado_final= adicionar_itens(lado_final,bote)
        
        elif escolha == "2":
            if "homem" not in lado_final:
                print("O homem nao esta no lado final!")
                continue

            print("Escolha um passageiro:")
            for i,item in enumerate(lado_final):
                if item != "homem":
                    print(f"{i} - {item}")
            print("ou pressione Enter para ir sozinho")

            escolha_passageiro = input()

            if escolha_passageiro == "":
                passageiro = None
            else:
                try:
                    indice = int(escolha_passageiro)
                    passageiro = lado_final[indice]
                    if passageiro == "homem":
                        print("O homem é quem dirige o barco! Escolha outro passageiro.")
                        continue
                except (ValueError, IndexError):
                    print("Escolha invalida!")
                    continue

            bote = preparar_bote(lado_final,passageiro)
            print(f"Bote atravessando com: {bote}")
            lado_inicial = adicionar_itens(lado_inicial,bote)

        elif escolha == "3":
            if "homem" not in lado_final:
                print("O homem nao esta no lado final!")
                continue

            bote = preparar_bote(lado_final)
            print(f"Bote atravessando com: {bote}")
            lado_inicial = adicionar_itens(lado_inicial,bote)

        elif escolha == "4":
            if "homem" not in lado_inicial:
                print("O homem nao esta no lado final!")
                continue

            bote = preparar_bote(lado_inicial)
            print(f"Bote atravessando com: {bote}")
            lado_final = adicionar_itens(lado_final,bote)

        elif escolha =="5":
            print("Saindo do jogo...")
            break

        else:
            print("Opção inválida! Tente novamente.")
            continue   
        mostrar_estado(lado_inicial,lado_final)

def fazer_travessia_automatica():
    """Executa as sequencias de travessias automaticamente com verificação opcional"""
    #estado inicial
    lado_inicial = ["homem", "lobo","maço de alfafa", "bode"]
    lado_final =[]

    print("=== Estado Inicial ===")
    mostrar_estado(lado_inicial,lado_final)

    #sequencias de travessias
    travessias =[
        ("bode", True),
        (None, False),
        ("maço de alfafa", True),
        ("bode",False),
        ("lobo", True),
        (None,False),
        ("bode", True)

    ]

    permitir_situacoes_inseguras = input("Permitir situaçoes inseguras temporarias? (s/n):").lower()

    for i, (passageiro, indo) in enumerate(travessias):
        print(f"\n === Passo {i+1} ===")

        if indo:
            print (f"Levando{passageiro if passageiro else 'ninguem'} do lado inicial para o final")
            bote = preparar_bote(lado_inicial,passageiro)
            print(f"bote atravessando com: {bote}")
            lado_final = adicionar_itens(lado_final, bote)
        else:
            print(f"Levando {passageiro if passageiro else 'ninguem'} do lado final para o inicial")
            bote = preparar_bote(lado_final, passageiro)
            print (f"Bote atravessadno com: {bote}")
            lado_inicial = adicionar_itens(lado_inicial, bote)

        mostrar_estado(lado_inicial, lado_final)

        #verificar situaçoes inseguras
        situacao_insegura_inicial = not verificar_estado_seguro(lado_inicial)
        situacao_insegura_final= not verificar_estado_seguro(lado_final)

        if( situacao_insegura_inicial or situacao_insegura_final) and not permitir_situacoes_inseguras:
            print("ATENÇAO: Situaçao insegura detectada! A travessia foi interrompida.")
            resposta = input("Deseja continuar mesmo assim? (s/n): ").lower()
            if resposta != 's':
                return
            
    print("\n=== Travessia concluida com sucesso! ===")

if __name__ == "__main__":
    print("Escolha o modo de travessia:")
    print("1 - Modo Interativo (você controla cada travessia)")
    print("2 - Modo Automatico (sequencia pre-definida)")

    escolha = input("Sua escolha: ")

    if escolha =="1":
        fazer_travessia_interativa()
    elif escolha =="2":
        fazer_travessia_automatica()
    else:
        print("Opção invalida!")

