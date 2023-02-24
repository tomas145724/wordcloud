# Libs

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
import requests

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import warnings
warnings.filterwarnings('ignore')
Image.open('americanas.png')


# Solução
def Buscar_Empresas(ticket):
  
  # Criando a URK
  Url = f'https://news.google.com/search?for={ticket}&hl=pt-BR&gl=BR&ceid=BR%3Apt-419'

  # Resposta
  Resposta = requests.get( Url )

  # Codigo --> SOAP
  Codigo_HTML = Resposta.text

  # Converter SOAP
  Objeto_Soup = BeautifulSoup( Codigo_HTML, 'html.parser')

  return Objeto_Soup

# Todas as informações
Dados = Buscar_Empresas('Americanas')

len( Dados )

# Buscando os titulos
Elementos = Dados.find_all('h3')

# Buscando os textos
Noticias = [ Texto.get_text() for Texto in Elementos ]

Concatenar = ''

for Loop in Noticias:
  Quebra = Loop.split()

  for Palavra in Quebra:
    Concatenar = Concatenar + ' ' + Palavra

Mascara = np.array( Image.open('americanas.png') )
Mascara[0:10]

# Criando a nuvem
Nuvem_Palavras = WordCloud(
  width= 1200,
  height= 1000,
  mask=Mascara,
  max_words=100,
  min_font_size=10,
  # Remover palavras
  stopwords=['Americanas', 'o', 'de', 'da', 'em', 'que', 'e', 'a', 'das', 'não', 'dos', 'Veja', 'sobre', 'AMER3', 'é', 'na', 'com', 'Por', 'as', 'os', 'como', 'do', 'para', 'no', 'à', 'R', 'se']
  ).generate( Concatenar )
 
Figura, Eixo = plt.subplots( figsize=(12, 10) )
plt.title('Nuvem de palavras - Americanas')
Eixo.imshow( Nuvem_Palavras, interpolation='bilinear' )
Eixo.set_axis_off()
plt.show()
#plt.savefig('Analise_Nuvem_Palavras.png')
