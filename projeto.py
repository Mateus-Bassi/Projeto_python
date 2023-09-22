import pandas as pd
from os import system

def reset(): # Funcionando
    global df_filtrado
    global lista_filtros
    print("-"*40)
    print("O DataFrame esta vazia depois de alguma filtragem.")
    reset = input("Deseja refazer a sua base de dados? Lembrando que vai precisar fazer todos os filtros novamente (sim ou nao): ").upper()
    if reset in ["S", "SIM"]:
        df_filtrado = df.copy()
        lista_filtros = []
    else:
        print("Finalizando o programa")
        exit()  # Use exit() para sair do programa

#Filtro Rank
def esc_rank():  # Funcionando 
    global df_filtrado
    while True:
        print("-"*40)
        print("     ->[Filtrando por Rank]<-     ")
        try:
            rank = int(input("Top o que voce escolhe?"))
            df_filtrado = df_filtrado[df_filtrado['Rank']<=rank]
            lista_filtros.append("Rank: "+ str(rank))
            system("cls") # Limpa a tela
            break
        except ValueError:
            print("Valor invalido. Tente novamente")


#Filtro Jogo
def esc_game(): # Funcionando em partes, opt 2 com erro 
    global df_filtrado
    global lista_filtros
    #system("cls") # Limpa a tela
    while True:
        try:
            print("-"*40)
            print("     ->[Filtrando por nome de jogo]<-     ")
            print("[1] Lista dos jogos\n[2] Filtrar por jogos\n[3] Sair")
            print("-"*40)
            opt = int(input("Opção:"))
            if opt == 1:
                print("     ->[Lista de Jogos Disponíveis]<-     ")
                print(set(df['Game']))
                print("-"*40)
                input("Pressione qualquer tecla para voltar ao menu de jogos: ")

            if opt == 2: 
                jogos_filtro = [jogo.strip() for jogo in input("Selecione os jogos separando por vírgula: ").split(",")]

                # Crie um DataFrame vazio para armazenar os resultados das filtragens dos jogos
                resultado_filtragem = pd.DataFrame()
                lista_filtros.append("Jogo(s): " + ', '.join(jogos_filtro))
                
                for jogo in jogos_filtro:
                    jogo_df = df_filtrado[df_filtrado['Game'].str.strip() == jogo]
                    resultado_filtragem = pd.concat([resultado_filtragem, jogo_df])

                df_filtrado = resultado_filtragem
                system("cls") # Limpa a tela
            if opt == 3:
                system("cls") # Limpa a tela
                break
        except ValueError:
            print("Opcao nao encontrada, tente de novo")

#filtro mes
def esc_Month():  # Funcionando 
    global df_filtrado
    global lista_filtros
    while True:
        try:
            meses = {1: "Janeiro",2: "Fevereiro",3: "Março",4: "Abril",5: "Maio",6: "Junho",7: "Julho",8: "Agosto",9: "Setembro",10: "Outubro",11: "Novembro",12: "Dezembro"}
            system("cls")
            print("-"*40)
            print("     ->[Filtrando por Mes]<-     \n")
            mes= int(input("[ 1] Janeiro\n[ 2] Fevereiro\n[ 3] Marco\n[ 4] Abril\n[ 5] Maio\n[ 6] Junho\n[ 7] Julho\n[ 8]Agosto\n[ 9] Setembro\n[10] Outubro\n[11] Novembro\n[12] Dezembro\nQual sua escolha?"))
            if mes > 12 or mes < 1:
                print("Valor invalido. Tente novamente")
            else:
                df_filtrado = df_filtrado[df_filtrado['Month']==mes]
                lista_filtros.append("Mes: "+ meses[mes])
                system("cls") # Limpa a tela
                break

        except ValueError:
            print("Valor invalido. Tente novamente")

#Filtro ano
def esc_year(): # funcionando 
    global df_filtrado
    global lista_filtros
    while True:
        try:
            
            print("     ->[Filtrando por ano]<-     ")
            ano = int(input("Qual ano voce escolhe? (2016 - 2023)\n"))
            if ano > 2023 or ano <2016: # errado
                print("Valor invalido. Tente novamente")
            else:             
                df_filtrado = df_filtrado[df_filtrado['Year']== ano]
                lista_filtros.append("Ano: "+ str(ano))
                system("cls") # Limpa a tela
                break 
        except ValueError:
            print("Valor invalido. Tente novamente")

#Adiciona Filtro 
def Filtro_add():
    global df_filtrado
    global lista_filtros
    while True:
        try:
            print("-"*40)
            print("     ->[Adicionar Filtro]<-     ")
            print(f"Filtros ja aplicados: {lista_filtros}")
            print("-"*40)
            escolha= int(input(f"Quais filtros vamos adicionar ?\n[1] Rank\n[2] Game(s)\n[3] Mes\n[4] Ano\nEscolha: "))
            if escolha == 1:
                esc_rank()
                break
            elif escolha == 2:
                esc_game()
                break
            elif escolha == 3:
                esc_Month()
                break
            elif escolha == 4:
                esc_year()
                break
            else:
                print("Opcao nao encontrada, tente novamente")
        except ValueError:
            print("Valor invalido tente novamente ")


#Abre o arquivo e salva na var. df
df = pd.read_csv("Twitch_game_data.csv", delimiter=",", encoding="ISO-8859-1")
df_filtrado = df.copy()
lista_filtros = []
system("cls") # Limpa a tela
#Menu principal
while True:
    try:
        print("-"*40)
        print("     ->[Menu Principal]<-     ")
        print(f"Filtros ja aplicados: {lista_filtros}")
        print("-"*40)
        escolha= int(input("Escolha uma das opcoes:\n[1] Adicionar Filtro\n[2] Imprimir Grafico\n[3] Limpar filtros\nEscolha:"))
        if escolha == 1:
            Filtro_add()
        elif escolha == 2:
            if df_filtrado.empty:  # Verifique se o DataFrame está vazio após a filtragem
                reset()
            else:
                #mostra o grafico tambem ...
                print(df_filtrado)
        elif escolha == 3: #Reset filtros e tambem da um reset na base de dados
            print("Se resetar você deve selecionar os parâmetros para a consulta novamente!")
            reset = input("Refazer base de dados [S/N]: ").upper()
            if reset in ["S", "SIM"]:
                df_filtrado = df.copy()
                lista_filtros = []
        else: 
            print("Valor invalido. Digite novamente")
    except ValueError:
        print("Valor invalido. Digite novamente")