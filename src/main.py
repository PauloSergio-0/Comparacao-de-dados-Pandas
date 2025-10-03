import pandas as pd
import os


geral = pd.read_csv("src/data/eleitores_geral.csv", sep=',', encoding='UTF-8',dtype={'TITULO_ELE': str})

relacao_antiga =  pd.read_csv("src/data/eleitores_bio.csv", sep=';', encoding='UTF-8',dtype={'TITULO_ELE': str})

eleitores_chamados = geral[geral['TITULO_ELE'].isin(relacao_antiga['TITULO_ELE'])]

verificacao = eleitores_chamados[['POSSUI_FOTO', 'POSSUI_ASSINATURA', 'POSSUI_DIGITAL']].eq(0).all(axis=1).map({True: "Não", False: "Sim"})

eleitores_chamados.insert(5, "CADASTROU_BIO", verificacao)

if not os.path.exists('src/data_final'):
    os.makedirs('src/data_final')
eleitores_chamados.to_csv("src/data_final/verificação Biometria 2ª zona virgula.csv", encoding="UTF-8", sep=",", index=False)