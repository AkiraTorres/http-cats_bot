# Importações
import tweepy
import random
import time
import var

# Tokens de autenticação da API
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Autenticação da API e criando um objeto
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Acessa o arquivo para randomizar as imagens
with open('http.txt') as _file:
    http = _file.read().split(",")

def cat():# Posta uma foto de gato aleatória por hora
    while(1 == 1):
        random.shuffle(http)                    # Aleatoriza um erro http dentro do array
        photo = "images/" + http[0] + ".jpg"    # Salva em uma variável o diretório da imagem
        api.update_with_media(photo)            # Tweeta a foto
        time.sleep(3600)

print("Perfeito")
cat()