"""
    Ter pelo menos 4 graficos
    Fazer a documentacao



    Funcao (campos com *args):
        
"""


import pandas as pd

def menu():
    print("Escolha as opcoes")


df = pd.read_csv("Twitch_game_data.csv", delimiter=",", encoding="ISO-8859-1")

# #df_teste = df[df["Hours_watched"] > 39936159]

# # print(df_teste)
# # print(set(df['Game']))

# #top 3, top 10, top 100

test = ['Grand Theft Auto V', 'League of Legends'] 

# #query
# for i in test:
#     df_game = df[df['Game'] == i]
# #df_game=df_game[df_game['Year']== 2023]
# print(df_game)
df_game = pd.DataFrame()

# Loop através da lista de jogos
for jogo in test:
    jogo_df = df[df['Game'] == jogo]
    df_game = pd.concat([df_game, jogo_df])

df_teste = df_game[df_game['Year'] == 2022]


df_teste2 = df_teste[["Game","Month", "Hours_watched"]]

print(df_teste2)
print('-'*40)
print(df_game)
