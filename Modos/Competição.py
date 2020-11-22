import time
import os

def modo_solo():
    
    listas = '''
    |------------------------------|
    |        Escolha o tema        |
    |        para competir:        |
    |                              |
    |    [1] Matemática            |
    |    [2] Linguagens            |
    |    [3] Ciências da Natureza  |
    |    [4] Ciências Humanas      |
    |    [5] Mix                   |
    |------------------------------|'''

    #SELECIONAR
    while 1:
        print(listas)
        opcao_lista = int(input("\nDigite a opção desejada: "))
        
        #OPÇÕES:
        if opcao_lista == 1:       #MATEMÁTICA
            os.system('clear') or None
            print("matemática")
            break
        elif opcao_lista == 2:     #LINGUAGENS
            os.system('clear') or None
            print(linguagens1, linguagens2, linguagens3, linguagens4, linguagens5, linguagens6)
            break
        elif opcao_lista == 3:     #CIENCIAS DA NATUREZA
            os.system('clear') or None
            print(natureza1, natureza2, natureza3, natureza4, natureza5)
            break
        elif opcao_lista == 4:     #CIÊNCIAS HUMANAS
            os.system('clear') or None
            print("humanas")    
            break
        elif opcao_lista == 5:     #MIX
            os.system('clear') or None
            print(linguagens1, natureza1, linguagens3, natureza3, linguagens5, natureza5)    
            break
        else:                     #OPÇÃO INVÁLIDA
            os.system('clear') or None
            print("\nOpção inválida! \nTente novamente.\n")
            time.sleep(2)
            os.system('clear') or None
    
modo_solo()
