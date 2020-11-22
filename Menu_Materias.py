import time
import os

def menu_materias():
    materias = '''
    |-----------------------------------|
    |        Selecione a matéria        |
    |             desejada:             |
    |                                   |
    |     [1] Matemática                |
    |     [2] Linguagens                |
    |     [3] Ciêcias da Natureza       |
    |     [4] Ciências Humanas          |
    |                                   |
    |     [0] Voltar ao Menu Inicial    |
    |-----------------------------------|'''


    #SELECIONAR
    while 1:
        print(materias)
        opcao_materia = int(input("\nDigite a opção desejada: "))
        
        #OPÇÕES
        if opcao_materia == 1:
            os.system('clear') or None
            print("matematica()")
        elif opcao_materia == 2:
            os.system('clear') or None
            print("linguagens()")
        elif opcao_materia == 3:
            os.system('clear') or None
            print("ciencias_natureza()")
        elif opcao_materia == 4:
            os.system('clear') or None
            print("ciencias_humanas()")
        elif opcao_materia == 0:
            os.system('clear') or None 
            menu_inicial()
        else:
            os.system('clear') or None
            print("\nOpção inválida! \nTente novamente.\n")
            time.sleep(2)
            os.system('clear') or None

menu_materias()