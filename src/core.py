# Importações
import tweepy
import time, requests, os, random
from datetime import datetime

HTTP_CATS_URL = "https://http.cat/" # Link para acessar a API do http.cat
#random.shuffle(http)

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

http = [100,101,200,201,202,204,205,206,207,300,301,302,303,304,
        305,307,400,401,402,403,404,405,406,408,409,410,411,412,
        413,414,415,416,417,418,420,421,422,423,424,425,426,429,
        431,444,450,451,499,500,501,502,503,504,506,507,508,509,
        510,511,599]

def down(url): # Acessa a API do http.cat e realiza o download da imagem 
    filename = 'temp.jpg'
    # url = HTTP_CATS_URL + http[i]
    request = requests.get(url, stream=True)
    with open (filename, "wb") as image:
        for chunk in request:
            image.write(chunk)

def cats():
    api = autentication()
    photo = 'temp.jpg'
    api.update_with_media(photo)

def main():
    while(True):
        for i in range(59):
            url = HTTP_CATS_URL + str(http[i])
            try:
                down(url)
            except:
                break        
            time.sleep(10)
            #cats()
            now = datetime.now()
            timen = now.strftime("%d/%m/%Y %H:%M:%S")
            print(f"{i}: Imagem {http[i]} postada as {timen} ")
        os.system('cls' if os.name == 'nt' else 'clear')
        #random.shuffle(http)

main()