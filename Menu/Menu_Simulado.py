import os
import time

def menu_simulado():
    simulados = '''
    |------------------------------|
    |       Selecione o modo       |
    |     de simulado desejado:    |
    |                              |
    |                              |
    |     [1] Mix                  |
    |     [2] Selecionado          |
    |                              |
    |  [0] Voltar ao Menu Inicial  |
    |------------------------------|'''

    #SELECIONAR
    while 1:
        print(simulados)
        opcao_simulado = int(input("\nDigite a opção desejada: "))
        
        #OPÇÕES
        if opcao_simulado == 1:
            os.system('clear') or None
            print("Mix()")
            break
        elif opcao_simulado== 2:
            os.system('clear') or None
            print("Selecionado()")
            break
        elif opcao_simulado == 0:
            os.system('clear') or None 
            menu_inicial()
        else:
            os.system('clear') or None
            print("\nOpção inválida! \nTente novamente.\n")
            time.sleep(2)
            os.system('clear') or None

menu_simulado()
