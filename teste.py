import pandas as pd
import os
import matplotlib.pyplot as plt

from matplotlib.ticker import FuncFormatter

def top_10_jogos_ano_atual(df):
    ano_atual = pd.Timestamp.now().year
    df_ano_atual = df[df["Year"] == ano_atual]
    
    # Agregando valores para obter a soma das horas assistidas por jogo
    df_grouped = df_ano_atual.groupby("Game")["Hours_watched"].sum().reset_index()

    # Pegando os top 10 jogos
    top_10 = df_grouped.nlargest(10, "Hours_watched")

    # Plotando o gráfico
    plt.figure(figsize=(15,7))
    plt.barh(top_10["Game"], top_10["Hours_watched"], color="blue")
    plt.xlabel('Horas Assistidas')
    plt.ylabel('Jogos')
    plt.title(f'Top 10 Jogos Mais Assistidos em {ano_atual}')
    plt.xlim(0, top_10["Hours_watched"].max() + (0.1 * top_10["Hours_watched"].max()))
    ax = plt.gca()
    ax.invert_yaxis()
    
    # Configurando os ticks do eixo X
    max_val = top_10["Hours_watched"].max()
    ax.set_xticks([0, max_val/4, max_val/2, 3*max_val/4, max_val, max_val + (0.1 * max_val)])
    
    plt.show()





def aplica_filtro(df, filtros):
    df_filtrado = df.copy()
    
    if 'Game' in filtros:
        df_filtrado = df_filtrado[df_filtrado['Game'].isin(filtros['Game'])]
    
    if 'Rank' in filtros:
        df_filtrado = df_filtrado[df_filtrado['Rank'] <= filtros['Rank']]
        
    if 'Month' in filtros:
        df_filtrado = df_filtrado[df_filtrado['Month'].isin(filtros['Month'])]

    if 'Year' in filtros:
        df_filtrado = df_filtrado[df_filtrado['Year'].isin(filtros['Year'])]
    
    return df_filtrado



def esc_year(filtros):
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
    try:
        while True:
            years_input = input("Digite os anos desejados, separados por vírgulas (ex: 2020,2021,2022): ")
            if years_input in ["2016","2017","2018","2019","2020","2021","2022","2023"]:
                years = [int(year.strip()) for year in years_input.split(",")]
                filtros['Year'] = years
                break
            else:
                print("Selecione um ano valido! (2016-2023)")
                print("-"*50)
                continue
        
    except ValueError:
        print("Entrada inválida! Por favor, insira anos válidos.")
    return filtros



def esc_month(filtros):
    os.system("cls" if os.name == "nt" else "clear")
    try:
        while True:
            print("---- Filtrando por Mês ----")
            print("-"*40)

            meses = {1: "Janeiro",2: "Fevereiro",3: "Março",4: "Abril",5: "Maio",6: "Junho",7: "Julho",8: "Agosto",9: "Setembro",10: "Outubro",11: "Novembro",12: "Dezembro"}
            print("[ 1] Janeiro\n[ 2] Fevereiro\n[ 3] Março\n[ 4] Abril\n[ 5] Maio\n[ 6] Junho\n[ 7] Julho\n[ 8]Agosto\n[ 9] Setembro\n[10] Outubro\n[11] Novembro\n[12] Dezembro")
            print("-"*40)

            month_input = input("Digite os meses desejados, separados por vírgulas (ex: 1,5,10): ")

            month = [int(month.strip()) for month in month_input.split(",")]
            for x in month:
                if x > 12 or x < 1:
                    print("Valor invalido. Tente novamente")
                    print("-"*50)
                    continue
            break

        lista_temp = []
        for chave in meses.items():
            for mes in month:
                if mes == chave[0]:
                    lista_temp.append(chave[1])

        if len(lista_temp) > 0:
            filtros['Month'] = lista_temp
            
    except ValueError:
        print("Entrada inválida! Por favor, insira anos válidos.")
    return filtros



def esc_rank(filtros):
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        try:
            print("---- Filtrando por Rank ----")
            rank = int(input("Informe o top ranking desejado (exemplo: para os top 10, digite 10): "))
            
            # Se tudo estiver correto, adicionamos o rank ao dicionário de filtros
            filtros['Rank'] = rank
            
            os.system("cls" if os.name == "nt" else "clear")
            return filtros
        except ValueError:
            print("Entrada inválida! Por favor, insira um rank válido.")



def esc_game(filtros):
    os.system("cls" if os.name == "nt" else "clear") # Limpa a tela
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

                if 'Game' in filtros:
                    filtros['Game'].extend(jogos_filtro)
                    filtros['Game'] = list(set(filtros['Game'])) # Remove registros duplicados
                else:
                    filtros['Game'] = jogos_filtro # Adiciona jogo no filtro
                
                os.system("cls" if os.name == "nt" else "clear") # Limpa a tela
                return filtros
            
            elif opcao == 3:
                os.system("cls" if os.name == "nt" else "clear") # Limpa a tela
                return filtros

        except ValueError:
            print("Opção não encontrada, tente de novo")



def menu_parametros(filtros):
    # Menu de escolha de parâmetros pelo usuário
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("---- Menu de Parâmetros ----")
            print("Escolha os parâmetros que serão usados na sua consulta:")
            print("[1] Rank\n[2] Game(s)\n[3] Mes\n[4] Ano")

            print("-"*40)
            print(f"Filtros aplicados: {filtros}")
            opcao_menu= int(input("Opção: "))

            #  Verificado aqui se a opção é inválida. Se for, a opção não é armazenada.
            if opcao_menu > 4 or opcao_menu <= 0:
                continue

            return opcao_menu
        except ValueError:
            print("Valor invalido. Digite novamente")


def menu(filtros):
    #  Menu principal onde o usuário escolhe se quer colocar parâmetros, limpar os filtros ou imprimir os gráficos.
    while True:
        try:
            print("---- Menu Principal ----")
            print("[1] Escolher parâmetros de consulta\n[2] Limpar filtros\n[3] Imprimir Grafico\n[4] Fechar o Programa")

            print("-"*40)
            print(f"Filtros aplicados: {filtros}")
            opcao_menu= int(input("Opção: "))

            #  Verificado aqui se a opção é inválida. Se for, a opção não é armazenada.
            if opcao_menu > 4 or opcao_menu <=0:
                continue

            return opcao_menu
        except ValueError:
            print("Valor invalido. Digite novamente")


def menu_graficos():
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("---- Menu de Gráficos ----")
            print("Escolha entre gráficos prontos e gráficos personalizados!")
            print("-"*40)
            print("[1] Top 10 de cada ano\n[2] Top\n[3] Mes\n[4] Ano")

            print("-"*40)
            print(f"Filtros aplicados: {filtros}")
            opcao_menu= int(input("Opção: "))

            #  Verificado aqui se a opção é inválida. Se for, a opção não é armazenada.
            if opcao_menu > 4 or opcao_menu <= 0:
                continue

            return opcao_menu
        except ValueError:
            print("Valor invalido. Digite novamente")

df = pd.read_csv("Twitch_game_data.csv", delimiter=";", encoding="ISO-8859-1")
df_filtrado = df.copy()

filtros = {}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    opcao_menu = menu(filtros)
    if opcao_menu == 1:
        # Aqui ocorrerá as operações envolvendo a escolha dos parâmetros para consulta pelo usuário.
        opcao_menu_param = menu_parametros(filtros)

        if opcao_menu_param == 1:
            # Escolha do Ranking
            filtros = esc_rank(filtros)
            pass
        elif opcao_menu_param == 2:
            # Escolha dos games
            filtros = esc_game(filtros)
            
        elif opcao_menu_param == 3:
            # Escolha do mes
            filtros = esc_month(filtros)
            
        elif opcao_menu_param == 4:
            # Escolha do ano
            filtros = esc_year(filtros)

    elif opcao_menu == 2:
        filtros = {} # Resetando Filtros
        print("Filtro Resetado com sucesso!")


    elif opcao_menu == 3:
        # Aqui terá a parte gráfica do programa.
        # Sugestão: Criar um arquivo separado contendo as funções gráficas, e apenas referenciar elas aqui
        # Se não houverem filtros, irá mostrar todo o df
        df_filtrado = aplica_filtro(df_filtrado, filtros)
        print("-"*50)
        top_10_jogos_ano_atual(df_filtrado)
        print("-"*50)
        input("Pressione qualquer tecla para voltar para o menu: ")
        ...


    if opcao_menu == 4:
        # Fechar o programa
        os.system("cls" if os.name == "nt" else "clear")
        print("Obrigado por usar o programa! =)")
        exit()
        