import pandas as pd
from os import system


def reset(df_filtrado, lista_filtros): # Funcionando
    print("Se resetar você deve selecionar os parâmetros para a consulta novamente!")
    reset = input("Refazer base de dados [S/N]: ").upper()
    if reset in ["S", "SIM"]:
        df_filtrado = df.copy()
        lista_filtros = []

        return df_filtrado, lista_filtros
    else:
        pass
        #  Creio que essa parte deve apenas preservar o DF, jogando o usuário para o menu novamente.

        # print("Finalizando o programa")
        # exit()  # Use exit() para sair do programa


def esc_game(df_filtrado, lista_filtros): 
    system("cls") # Limpa a tela
    while True:
        try:
            print("---- Filtrando por nome de jogo ----")
            print("[1] Lista dos jogos\n[2] Filtrar por jogos\n[3] Voltar ao menu de parâmetros")
            print("-"*40)

            opcao = int(input("Opção:"))

            if opcao == 1:
                print("---- Lista de Jogos Disponíveis ----")
                print(set(df['Game']))
                print("-"*40)
                input("Pressione qualquer tecla para voltar ao menu de jogos: ")

            elif opcao == 2: 
                jogos_filtro = [jogo.strip() for jogo in input("Selecione os jogos separando por vírgula: ").split(",")]

                # Crie um DataFrame vazio para armazenar os resultados das filtragens dos jogos
                resultado_filtragem = pd.DataFrame()
                lista_filtros.append("Jogo(s): " + ', '.join(jogos_filtro))
                
                for jogo in jogos_filtro:
                    jogo_df = df_filtrado[df_filtrado['Game'].str.strip() == jogo]
                    resultado_filtragem = pd.concat([resultado_filtragem, jogo_df])

                df_filtrado = resultado_filtragem
                system("cls") # Limpa a tela

                return df_filtrado, lista_filtros
            
            elif opcao == 3:
                system("cls") # Limpa a tela
                return df_filtrado, lista_filtros

        except ValueError:
            print("Opção não encontrada, tente de novo")


def menu_parametros(lista_filtros):
    # Menu de escolha de parâmetros pelo usuário
    while True:
        try:
            print("---- Menu de Parâmetros ----")
            print("Escolha os parâmetros que serão usados na sua consulta:")
            print("[1] Rank\n[2] Game(s)\n[3] Mes\n[4] Ano\n[5] Horas assistidas")

            print("-"*40)
            print(f"Filtros aplicados: {lista_filtros}")
            opcao_menu= int(input("Opção: "))

            #  Verificado aqui se a opção é inválida. Se for, a opção não é armazenada.
            if opcao_menu > 5 or opcao_menu <= 0:
                continue

            return opcao_menu
        except ValueError:
            print("Valor invalido. Digite novamente")


def menu(lista_filtros):
    #  Menu principal onde o usuário escolhe se quer colocar parâmetros, limpar os filtros ou imprimir os gráficos.
    while True:
        try:
            print("---- Menu Principal ----")
            print("[1] Escolher parâmetros de consulta\n[2] Limpar filtros\n[3] Imprimir Grafico\n[4] Fechar o Programa")

            print("-"*40)
            print(f"Filtros aplicados: {lista_filtros}")
            opcao_menu= int(input("Opção: "))

            #  Verificado aqui se a opção é inválida. Se for, a opção não é armazenada.
            if opcao_menu > 4 or opcao_menu <=0:
                continue

            return opcao_menu
        except ValueError:
            print("Valor invalido. Digite novamente")


df = pd.read_csv("Twitch_game_data.csv", delimiter=";", encoding="ISO-8859-1")
df_filtrado = df.copy()

lista_filtros = []

while True:
    opcao_menu = menu(lista_filtros)
    if opcao_menu == 1:
        # Aqui ocorrerá as operações envolvendo a escolha dos parâmetros para consulta pelo usuário.
        opcao_menu_param = menu_parametros(lista_filtros)

        if opcao_menu_param == 1:
            # Escolha do Ranking
            pass
        elif opcao_menu_param == 2:
            # Escolha dos games
            df_filtrado, lista_filtros = esc_game(df_filtrado, lista_filtros)
            pass
        elif opcao_menu_param == 3:
            # Escolha do mes
            pass
        elif opcao_menu_param == 4:
            # Escolha do ano
            pass
        elif opcao_menu_param == 5:
            # Escolha das horas assistidas
            pass


    elif opcao_menu == 2:
        # Reseta o DataFrame e a lista de filtros
        # A função reset está retornando um elemento duplo
        df_filtrado, lista_filtros = reset(df_filtrado, lista_filtros)
        print("Filtro Resetado com sucesso!")
        input("Pressione qualquer tecla para continuar: ")


    elif opcao_menu == 3:
        # Aqui terá a parte gráfica do programa.
        # Sugestão: Criar um arquivo separado contendo as funções gráficas, e apenas referenciar elas aqui
        if df_filtrado.empty:
            # Se o DataFrame estiver vazio, imprimir mensagem avisando o usuário que essa opção não é possível
            print("Não há parâmetros para a consulta. Por favor selecione os campos desejados no menu!")
            input("Pressione qualquer tecla para ir para a tela de seleção de parâmetros: ")
            continue
        else:
            # **** Colocar a parte gráfica aqui ****
            print(df_filtrado)
        ...


    if opcao_menu == 4:
        # Fechar o programa
        pass     
        
