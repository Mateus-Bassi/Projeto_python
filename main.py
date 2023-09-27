# William Dalla Stella dos Santos
# Mateus Stanislauki Bassi
# Vinicius Shigueyuki Ito
# Juan Vitor Peres

import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def formato_personalizado(x, pos):
    # Função para formatar os números em milhões
    if x >= 1e9:  # Bilhões
        return f'{x*1e-9:.1f}B'
    elif x >= 1e6:  # Milhões
        return f'{x*1e-6:.1f}M'
    elif x >= 1e3:  # Milhares
        return f'{x*1e-3:.0f}K'
    else:  # Caso o número seja menor que mil
        return f'{x:.0f}'
    

def grafico_personalizado(df):
    # Monta o gráfico onde o usuário escolhe o eixo X
    # O nome dos jogos sempre será o eixo Y para esse gráfico
    opcoes = {
        1: "Hours_watched",
        2: "Hours_streamed",
        3: "Peak_viewers",
        4: "Peak_channels",
        5: "Streamers",
        6: "Avg_viewers",
        7: "Avg_channels"
    }

    while True:
        try:
            # O usuário deve escolher o ano e depois o top X jogos
            os.system("cls" if os.name == "nt" else "clear")
            ano = int(input("Ano: "))
            ranking = int(input("Top: "))
            
            print("---- Gráfico Personalizado ----")
            print("Escolha o Eixo X: ")
            print("[1] Horas assistidas")
            print("[2] Horas de Stream")
            print("[3] Máximo de viewers assistindo simultaneamente")
            print("[4] Máximo de canais abertos simultaneamente")
            print("[5] Número de Streamers")
            print("[6] Média de espectadores")
            print("[7] Média de espectadores por canal")
            print("-"*40)

            eixo_x = int(input("Opção: "))
            
            if 1 <= eixo_x <= 7:
                break
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("Opções inválidas.")
                print("-"*40)
                    
        except ValueError:
            os.system("cls" if os.name == "nt" else "clear")
            print("Entrada inválida.")
            print("-"*40)              

    # Filtra todos os jogos do ano
    df_filtrado1 = df[df['Year'] == ano] 
    # Filtra pelo ranking os jogos do ano escolhido
    df_filtrado1 = df_filtrado1[df_filtrado1['Rank'] <= ranking] 
    
     # Agrupa por jogo e soma as horas assistidas
    df_agrupado  = df_filtrado1.groupby('Game').sum().reset_index()    

    for chave, valor in opcoes.items():
            if eixo_x == chave:
                # Ordenando o DF pelo valor escolhido
                df_top = df_agrupado.sort_values(by=valor, ascending=False).head(ranking)

                # Plotando o gráfico
                plt.figure(figsize=(10, 6))
                plt.barh(df_top["Game"], df_top[valor], color='skyblue')
                plt.xlabel(valor)
                plt.title(f"{valor} dos Top {ranking} Jogos de {ano}")
                plt.gca().invert_yaxis()  # Inverte o eixo y para o jogo com mais horas fique no topo

            
                # A função FuncFormatter espera que a função recebida tenha dois parâmetros
                    # Arg1 = valor a ser formatado
                    # Arg2 = posição do elemento
                # Função para formatar os valores do Eixo X para milhares, milhões ou bilhões
                formatador = FuncFormatter(formato_personalizado)           

                # Atribuindo para o formatador padrão o formatador criado
                plt.gca().xaxis.set_major_formatter(formatador)
                plt.tight_layout()
                plt.show()



def grafico_top_10_horas(df):
    #  Gráfico que mostra os TOP 10 jogos de determinado ano pelas horas assistidas

    ano = int(input("Ano: "))
    df_ano = df[df['Year'] == ano]
    
    # Agrupa por jogo e soma as horas assistidas
    df_agrupado  = df_ano.groupby('Game').sum().reset_index()

    # Ordenando o DF pelas horas assistidas
    df_top_10 = df_agrupado.sort_values(by="Hours_watched", ascending=False).head(10)

    # Plotando o gráfico
    plt.figure(figsize=(10, 6))
    plt.barh(df_top_10["Game"], df_top_10["Hours_watched"], color='skyblue')
    plt.xlabel("Horas Assistidas")
    plt.title(f"Horas Assistidas dos Top 10 Jogos de {ano}")
    plt.gca().invert_yaxis()  # Inverte o eixo y para que o jogo com mais horas fique no topo

   
    # A função FuncFormatter espera que a função recebida tenha dois parâmetros
        # Arg1 = valor a ser formatado
        # Arg2 = posição do elemento
    # Função para formatar os valores do Eixo X para milhares, milhões ou bilhões
    formatador = FuncFormatter(formato_personalizado)           

    # Atribuindo para o formatador padrão o formatador criado
    plt.gca().xaxis.set_major_formatter(formatador)
    plt.tight_layout()
    plt.show()



def grafico_top_10_streamed(df):
    #  Gráfico que mostra os TOP 10 jogos de determinado ano pelas horas de stream

    ano = int(input("Ano: "))
    df_ano = df[df['Year'] == ano]
    
    # Agrupa por jogo e soma as horas de stream
    df_agrupado  = df_ano.groupby('Game').sum().reset_index()

    # Ordenando o DF pelas horas de stream
    df_top_10 = df_agrupado.sort_values(by="Hours_streamed", ascending=False).head(10)

    # Plotando o gráfico
    plt.figure(figsize=(10, 6))
    plt.barh(df_top_10["Game"], df_top_10["Hours_streamed"], color='skyblue')
    plt.xlabel("Horas streamed")
    plt.title(f"Horas streamed dos Top 10 Jogos de {ano}")
    plt.gca().invert_yaxis()  # Inverte o eixo y para o jogo com mais horas fique no topo

    # A função FuncFormatter espera que a função recebida tenha dois parâmetros
        # Arg1 = valor a ser formatado
        # Arg2 = posição do elemento
    # Função para formatar os valores do Eixo X para milhares, milhões ou bilhões
    formatador = FuncFormatter(formato_personalizado)           

    # Atribuindo para o formatador padrão o formatador criado
    plt.gca().xaxis.set_major_formatter(formatador)
    plt.tight_layout()
    plt.show()



def grafico_meses_mais_assistidos(df):
    # Gráfico que mostra os meses mais assistidos de determinado ano

    ano = int(input("Ano: "))
    df_ano = df[df['Year'] == ano]
    
    # Agrupa por mês e por horas assitidas
    df_agrupado  = df_ano.groupby('Month').sum().reset_index()

    # Ordenando o DF pelas horas de stream
    df_top_mes = df_agrupado.sort_values(by="Hours_watched", ascending=False).head(12)

    # Plotando o gráfico
    plt.figure(figsize=(10, 6))
    plt.barh(df_top_mes["Month"], df_top_mes["Hours_watched"], color='skyblue')
    plt.xlabel("Horas assistidas")
    plt.title(f"Meses mais assistidos de {ano}")
    plt.gca().invert_yaxis()  # Inverte o eixo y para o jogo com mais horas fique no topo

   
    # A função FuncFormatter espera que a função recebida tenha dois parâmetros
        # Arg1 = valor a ser formatado
        # Arg2 = posição do elemento
    formatador = FuncFormatter(formato_personalizado)
    plt.gca().xaxis.set_major_formatter(formatador)

    plt.tight_layout()
    plt.show()



def aplica_filtro(df, filtros):
    # Filtra o DF pelo campo escolhido pelo usuário

    df_filtrado = df.copy()
    
    if 'Game' in filtros:
        #  Uso de isin para filtra com base em uma lista de valores (caso escolha mais de um jogo)
        df_filtrado = df_filtrado[df_filtrado['Game'].isin(filtros['Game'])]
    
    if 'Rank' in filtros:
        # Filtra todos os rankins que forem menor ou igual ao número escolhido pelo usuário
        df_filtrado = df_filtrado[df_filtrado['Rank'] <= filtros['Rank']]
        
    if 'Month' in filtros:
        #  Uso de isin para filtra com base em uma lista de valores (caso escolha mais de um mes)
        df_filtrado = df_filtrado[df_filtrado['Month'].isin(filtros['Month'])]

    if 'Year' in filtros:
        #  Uso de isin para filtra com base em uma lista de valores (caso escolha mais de um ano)
        df_filtrado = df_filtrado[df_filtrado['Year'].isin(filtros['Year'])]
    
    return df_filtrado




def esc_year(filtros):
    # Recebe um dicionário filtros e adiciona uma lista com os valores dos anos que o usuário deseja
    while True:
        try:
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
    # Recebe um dicionário filtros e adiciona uma lista com os valores dos meses que o usuário deseja
    os.system("cls" if os.name == "nt" else "clear")
    try:
        while True:
            print("---- Filtrando por Mês ----")
            print("-"*40)

            #  Dicionário para o usuário escolher o mês pelo número e o programa entender o mês referenciado
            dict_month = {1: "Janeiro",
                          2: "Fevereiro",
                          3: "Março",
                          4: "Abril",
                          5: "Maio",
                          6: "Junho",
                          7: "Julho",
                          8: "Agosto",
                          9: "Setembro",
                          10:"Outubro",
                          11:"Novembro",
                          12:"Dezembro"
                        }

            print("[ 1] Janeiro")
            print("[ 2] Fevereiro")
            print("[ 3] Março")
            print("[ 4] Abril")
            print("[ 5] Maio")
            print("[ 6] Junho")
            print("[ 7] Julho")
            print("[ 8] Agosto")
            print("[ 9] Setembro")
            print("[10] Outubro")
            print("[11] Novembro")
            print("[12] Dezembro")
            print("-"*40)

            month_input = input("Digite os meses desejados, separados por vírgulas (ex: 1,5,10): ")

            list_month = [int(month.strip()) for month in month_input.split(",")]
            for x in list_month:
                if x > 12 or x < 1:
                    print("Valor invalido. Tente novamente")
                    print("-"*50)
                    continue
            break

        
        lista_temp = []
        for chave in dict_month.items():
            for mes in list_month:
                if mes == chave[0]:
                    # Adiciona o valor do mês na lista temporária
                    lista_temp.append(chave[1])

        # Adiciona no dicionário caso a lista não esteja vazia
        if len(lista_temp) > 0:
            filtros['Month'] = lista_temp
            
    except ValueError:
        print("Entrada inválida! Por favor, insira anos válidos.")
    return filtros



def esc_rank(filtros):
    # Recebe um dicionário filtros e adiciona o valor do TOP X que o usuário deseja
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
    # Recebe um dicionário filtros e adiciona uma lista com os valores dos jogos que o usuário deseja

    os.system("cls" if os.name == "nt" else "clear")
    while True:
        try:
            print("---- Filtrando por nome de jogo ----")
            print("[1] Lista dos jogos")
            print("[2] Filtrar por jogos")
            print("[3] Voltar ao menu de parâmetros")
            print("-"*40)

            opcao = int(input("Opção:"))

            if opcao == 1:
                # Mostra todos os jogos para o usuário
                os.system("cls" if os.name == "nt" else "clear")
                print("---- Lista de Jogos Disponíveis ----")
                print(set(df['Game']))
                print("-"*40)
                input("Pressione qualquer tecla para voltar ao menu de jogos: ")


            elif opcao == 2: 
                jogos_filtro = [jogo.strip() for jogo in input("Selecione os jogos separando por vírgula: ").split(",")]

                # Adiciona o jogo sem soprepor outros jogos já selecionados
                if 'Game' in filtros:
                    filtros['Game'].extend(jogos_filtro)
                    filtros['Game'] = list(set(filtros['Game'])) # Remove registros duplicados
                else:
                    filtros['Game'] = jogos_filtro # Adiciona jogo no filtro
                
                os.system("cls" if os.name == "nt" else "clear")
                return filtros
            
            elif opcao == 3:
                # Retorna ao menu principal
                os.system("cls" if os.name == "nt" else "clear")
                return filtros

        except ValueError:
            print("Opção não encontrada, tente de novo")



def menu_filtros(filtros):
    # Menu de escolha de parâmetros pelo usuário
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("---- Menu de Filtros ----")
            print("Escolha os filtros que serão usados na sua consulta:")
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



def menu_personalizado(filtros):
    #  Menu principal onde o usuário escolhe se quer colocar parâmetros, limpar os filtros ou imprimir os gráficos.
    try:
        os.system("cls" if os.name == "nt" else "clear")
        print("---- Menu Personalizado ----")
        print("[1] Escolher filtros")
        print("[2] Limpar filtros")
        print("[3] Imprimir Consulta")
        print("[4] Voltar para o menu de gráficos")
        print("-"*40)

        print(f"Filtros aplicados: {filtros}")
        opcao_menu= int(input("Opção: "))

        #  Verificado aqui se a opção é inválida. Se for, a opção não é armazenada.
        if opcao_menu > 4 or opcao_menu <=0:
            return

        return opcao_menu
    except ValueError:
        print("Valor invalido. Digite novamente")



def menu_graficos():
    #  Menu de gráficos onde o usuário escolhe o tipo de gráfico que ele quer
    #  A opção 5 é um bônus onde o usuário pode realizar uma consulta e filtrar os dados
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("---- Menu de Gráficos ----")
            print("Escolha entre gráficos prontos e gráficos personalizados!")
            print("-"*40)

            print("[1] Top 10 jogos mais assistidos de determinado ano")
            print("[2] Top 10 jogos mais streamed de determinado ano")
            print("[3] Ranking de Meses mais assistidos de determinado ano")
            print("[4] Gráfico Personalizado")
            print("")
            print("[5] Mostrar consulta no terminal")
            print("[6] Sair do programa")

            print("-"*40)
            opcao_menu= int(input("Opção: "))

            #  Verificado aqui se a opção é inválida. Se for, a opção não é armazenada.
            if opcao_menu > 6 or opcao_menu <= 0:
                continue

            return opcao_menu
        except ValueError:
            print("Valor invalido. Digite novamente")



df = pd.read_csv("Twitch_game_data.csv", delimiter=";", encoding="ISO-8859-1")
df_filtrado = df.copy()

filtros = {}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    opcao_graficos = menu_graficos()

    if opcao_graficos == 1:
        grafico_top_10_horas(df_filtrado)

    elif opcao_graficos == 2:
        grafico_top_10_streamed(df_filtrado)
    elif opcao_graficos == 3:
        grafico_meses_mais_assistidos(df_filtrado)

    elif opcao_graficos == 4:
        #  Personalizado
        grafico_personalizado(df_filtrado)
            
        
    elif opcao_graficos == 5:
        while True:
            opcao_menu = menu_personalizado(filtros)
            if not opcao_menu:
                continue
            if opcao_menu == 1:
                # Aqui ocorrerá as operações envolvendo a escolha dos parâmetros para consulta pelo usuário.
                opcao_menu_filtros = menu_filtros(filtros)

                if opcao_menu_filtros == 1:
                    # Escolha do Ranking
                    filtros = esc_rank(filtros)
                    
                elif opcao_menu_filtros == 2:
                    # Escolha dos games
                    filtros = esc_game(filtros)
                    
                elif opcao_menu_filtros == 3:
                    # Escolha do mes
                    filtros = esc_month(filtros)
                    
                elif opcao_menu_filtros == 4:
                    # Escolha do ano
                    filtros = esc_year(filtros)

            elif opcao_menu == 2:
                filtros = {} # Resetando Filtros
                print("Filtro Resetado com sucesso!")


            elif opcao_menu == 3:
                # Aplica os filtros e filtra o DF
                df_filtrado = aplica_filtro(df_filtrado, filtros)
                print("-"*50)
                
                print(df_filtrado)

                print("-"*50)
                input("Pressione qualquer tecla para voltar para o menu: ")

            elif opcao_menu == 4:
                break

    elif opcao_graficos == 6:
        # Fechar o programa
        os.system("cls" if os.name == "nt" else "clear")
        print("Obrigado  por usar o programa! =)")
        exit()
