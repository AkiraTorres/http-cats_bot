# Importações
import tweepy
import random
import time
import requests
from datetime import datetime

HTTP_CATS_URL = "https://http.cat/" # Link para acessar a API do http.cat

def autentication():    # Função que faz a autenticação da API com o twitter
    # Tokens de autenticação da API
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    # Processo de autenticação
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)  # Criação de um objeto api
    return api

http = [100,101,103,200,201,202,203,204,205,206,300
        ,301,302,303,304,307,308,400,401,402,403,404
        ,405,406,407,408,409,410,411,412,413,414,415
        ,416,417,418,422,425,426,428,429,431,451,500
        ,501,502,503,504,505,506,507,508,510,511]

def down(): # Acessa a API do http.cat e realiza o download da imagem 
    filename = 'temp.jpg'
    url = HTTP_CATS_URL + http[i]
    request = requests.get(url, stream=True)
    with open (filename, "wb") as image:
        for chunk in request:
            image.write(chunk)

def cats():
    api = autentication()
    photo = 'temp.jpg'
    api.update_with_media(photo)

def main():
    a = 0
    while(True):
        random.shuffle(http)
        for i in http:
            #a += 1
            down()
            cats()
            now = datetime.now()
            timen = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Imagem postada as ", timen)
            #print(a)
            time.sleep(300)

#main()
print(http)