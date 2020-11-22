import time
import os

def menu_incial():
    inicio = '''
    |-------------------------------|
    |          xxxxxxxxxx           |
    |          xxxxxxxxxx           |
    |                               |
    | [1] Resumos/Exercicíos        |
    | [2] Competição                |
    | [3] Simulados                 |
    | [4] Créditos                  |
    |-------------------------------|'''

    ##SELECIONAR
    while 1:
        print(inicio)
        opcao_menu = int(input("\nDigite a opção desejada: "))
        
        #OPÇÕES:
        if opcao_menu == 1:       #RESUMOS/EXERCÍCIOS
            os.system('clear') or None
            menu_materias()
            break
        elif opcao_menu == 2:      #COMPETIÇÃO
            os.system('clear') or None
            print("DESENVOLVENDO")
            break
        elif opcao_menu == 3:      #SIMULADOS
            os.system('clear') or None
            print("DESENVOLVENDO")
            break
        elif opcao_menu == 4:      #CRÉDITOS
            os.system('clear') or None
            print("DESENVOLVENDO")      
            break
        else:
            os.system('clear') or None
            print("\nOpção inválida! \nTente novamente.\n")
            time.sleep(2)
            os.system('clear') or None

menu_incial()