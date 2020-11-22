import time
import os

def menu():
    def menu_inicial():
        inicio = '''
        |------------------------------|
        |        |Enem -------|        |
        |        |---- Estudei|        |
        |                              |
        |    [1] Resumos/Exercicíos    |
        |    [2] Competição            |
        |    [3] Simulados             |
        |    [4] Créditos              |
        |------------------------------|'''

        #SELECIONAR
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
                menu_competicao()
                break
            elif opcao_menu == 3:      #SIMULADOS
                os.system('clear') or None
                menu_simulado()
                break
            elif opcao_menu == 4:      #CRÉDITOS
                os.system('clear') or None
                menu_creditos()    
                break
            else:
                os.system('clear') or None
                print("\nOpção inválida! \nTente novamente.\n")
                time.sleep(2)
                os.system('clear') or None

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
                print(matematica())
                break
            elif opcao_materia == 2:
                os.system('clear') or None
                print("linguagens()")
                break
            elif opcao_materia == 3:
                os.system('clear') or None
                print(c_natureza())
                break
            elif opcao_materia == 4:
                os.system('clear') or None
                print(c_humanas())
                break
            elif opcao_materia == 0:
                os.system('clear') or None 
                menu_inicial()
            else:
                os.system('clear') or None
                print("\nOpção inválida! \nTente novamente.\n")
                time.sleep(2)
                os.system('clear') or None

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
                break
            elif opcao_competicao == 2:
                os.system('clear') or None
                print("ModoVersus()")
                break
            elif opcao_competicao == 3:
                os.system('clear') or None
                print("ModoVersusCriativo()")
                break
            elif opcao_competicao == 0:
                os.system('clear') or None 
                menu_inicial()
            else:
                os.system('clear') or None
                print("\nOpção inválida! \nTente novamente.\n")
                time.sleep(2)
                os.system('clear') or None
  
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
    
    def menu_creditos():
        os.system('clear') or None
        print("Jogo desenvolvido por alunos da Universidade Presbiteriana Mackenzie. \n")
        time.sleep(3)
        print("Francis Kenji Teruya          TIA: 41912055")
        time.sleep(1)        
        print("Guilherme Heitor Pensutti     TIA: 41921704")
        time.sleep(1)
        print("João Vitor Duarte Queiroz     TIA: 41930096") 
        time.sleep(4)
        os.system('clear') or None
        menu_inicial()
    
    menu_inicial()
menu()
