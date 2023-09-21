import pandas as pd
from os import system

def reset(): # Funcionando
    global df_filtrado
    global list_app_filtros
    print("O DataFrame esta vazia depois de alguma filtragem.")
    reset = input("Deseja refazer a sua base de dados? Lembrando que vai precisar fazer todos os filtros novamente (sim ou nao): ").upper()
    if reset == "SIM":
        df_filtrado = df.copy()
        list_app_filtros = []
    else:
        print("Finalizando o programa")
        exit()  # Use exit() para sair do programa

#Filtro Rank
def esc_rank(): # funcionando
    global df_filtrado
    while True:
        system("cls") # Limpa a tela
        print("---- Filtrando por Rank ----")
        try:
            rank = int(input("Top o que voce escolhe?"))
            df_filtrado = df_filtrado[df_filtrado['Rank']<=rank]
            list_app_filtros.append("Rank: "+ str(rank))
            break
        except ValueError:
            print("Valor invalido. Tente novamente")


#Filtro Jogo
def esc_game(): # Funcionando em partes 
    global df_filtrado
    system("cls") # Limpa a tela
    while True:
        try:
            print("---- Filtranmdo por nome de jogo ----")
            print("1- Lista dos jogos\n2- Filtrar por jogos\n3- Sair")
            opt = int(input("Digite uma escolha:"))
            if opt == 1:
                print(set(df['Game']))
            if opt == 2: 
                jogos_filtro = input("Qual jogo(s) vamos filtrar? Caso escolha mais de 1 pode separe por ','.").split(",")
                # Crie um DataFrame vazio para armazenar os resultados das filtragens dos jogos
                resultado_filtragem = pd.DataFrame()
                list_app_filtros.append("Jogo(s): "+ str(jogos_filtro))
                for jogo in jogos_filtro:
                    jogo_df = df_filtrado[df_filtrado['Game'] == jogo]
                    resultado_filtragem = pd.concat([resultado_filtragem, jogo_df])

                df_filtrado = resultado_filtragem
                system("cls") # Limpa a tela
            if opt == 3:
                system("cls") # Limpa a tela
                break
        except ValueError:
            print("Opcao nao encontrada, tente de novo")

#filtro mes
def esc_mounth():  # Fazer
    global df_filtrado
    while True:
        try:
            ...
        except ValueError:
            print("Valor invalido. Tente novamente")

#Filtro ano
def esc_year(): # funcionando 
    global df_filtrado
    while True:
        try:
            system("cls") # Limpa a tela
            print("---- Filtrando por ano ----")
            ano = int(input("Qual ano voce escolhe? (2016 - 2023)\n"))
            if ano > 2023 or ano <2016: # errado
                print("Valor invalido. Tente novamente")
            else:             
                df_filtrado = df_filtrado[df_filtrado['Year']== ano]
                list_app_filtros.append("Ano: "+ str(ano))
                system("cls") # Limpa a tela
                break 
        except ValueError:
            print("Valor invalido. Tente novamente")

#Filtro Horas assistidas 
def esc_hours_wath(): # Fazer
    while True:
        global df_filtrado
        try:
            ...
        except ValueError:
            print("Valor invalido. Tente novamente")

#funcao de escolher os filtros
def menu(): # Funcionando 
    while True:
        try:
            print("---- Menu Principal ----")
            print("Escolha as opcoes")
            print(f"Como vamos filtrar?filtros ja aplicados: {list_app_filtros}")
            escolha= int(input("1-Rank\n2-Game(s)\n3-Mes\n4-Ano\n5-Horas assistidas\n6-Imprimir Grafico\nEscolha:"))
            if escolha == 1:
                esc_rank()
            if escolha == 2:
                esc_game()
            if escolha == 3:
                esc_mounth()
            if escolha == 4:
                esc_year()
            if escolha == 5:
                esc_hours_wath()
            if escolha == 6:
                if df_filtrado.empty:  # Verifique se o DataFrame está vazio após a filtragem
                    reset()
                else:
                    print(df_filtrado)
            if escolha == 7: #Reset filtros
                list_app_filtros = []
                df_filtrado = df.copy()
            if escolha >=8 or escolha <=0:
                print("Valor invalido. Digite novamente")
        except ValueError:
            print("Valor invalido. Digite novamente")

#abre o arquivo e salva na var. df
df = pd.read_csv("Twitch_game_data.csv", delimiter=",", encoding="ISO-8859-1")
df_filtrado = df.copy()
list_app_filtros = []
system("cls") # Limpa a tela
menu()