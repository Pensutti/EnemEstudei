import time
import os

def menu_competicao():
    competicao ='''
    |------------------------------------|
    |        Selecione o modo de         |
    |        competição desejado:        |
    |                                    |
    |     [1] Modo Solo                  |
    |     [2] Modo Versus                |
    |     [3] Modo Versus Criativo       |
    |                                    |
    |     [0] Voltar ao Menu Inicial     |
    |------------------------------------|'''

    #SELECIONAR
    while 1:
        print(competicao)
        opcao_competicao = int(input("\nDigite a opção desejada: "))
        
        #OPÇÕES
        if opcao_competicao == 1:
            os.system('clear') or None
            print("ModoSolo()")
        elif opcao_competicao == 2:
            os.system('clear') or None
            print("ModoVersus()")
        elif opcao_competicao == 3:
            os.system('clear') or None
            print("ModoVersusCriativo()")
        elif opcao_competicao == 0:
            os.system('clear') or None 
            menu_inicial()
            break
        else:
            os.system('clear') or None
            print("\nOpção inválida! \nTente novamente.\n")
            time.sleep(2)
            os.system('clear') or None

menu_competicao()
