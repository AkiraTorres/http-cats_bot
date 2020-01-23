# Importações
import tweepy
import random
import time
import requests

HTTP_CATS_URL = "https://http.cat/" # Link para acessar a API do http.cat

def autentication():    # Função que faz a autenticação da API com o twitter
    # Tokens de autenticação da API
    consumer_key = "226fpnITvzsxe70EcXZ6VftSq"
    consumer_secret = "4Q1AS3cSJOKvw4LYqxxDlAEkT2kH0PWawoHLrvS6su5Y1k2uum"
    access_token = "1220061094947033089-IOegfYGQgUeelQam3yLyPc0xPi7fo7"
    access_token_secret = "tCdI1nCtjMkaND2jfUPw2WF6KaWJTyubVEVL2yjE2DrTM"
    # Processo de autenticação
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)  # Criação de um objeto api
    return api

# Acessa o arquivo para randomizar entre as imagens
with open('http.txt') as _file:
    http = _file.read().split(",")
    random.shuffle(http)

def down(): # Acessa a API do http.cat e realiza o download da imagem 
    random.shuffle(http)
    filename = 'temp.jpg'
    url = HTTP_CATS_URL + http[0]
    request = requests.get(url, stream=True)
    with open (filename, "wb") as image:
        for chunk in request:
            image.write(chunk)

def cats():
    api = autentication()
    photo = 'temp.jpg'
    api.update_with_media(photo)

print("Perfeito")
while(True):
    down()
    cats()
    time.sleep(3600)