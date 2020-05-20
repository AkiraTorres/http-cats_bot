# Cats Http Bot

Esse é um Bot que posta uma fotos de gatos relacionadas a erros de http a cada uma hora no
[@CatsHttp_Bot](https://twitter.com/CatsHttp_Bot) 
 
![404](https://http.cat/404)

## Instalando e executando

Primeiro é necessário instalar o python 3 e o pip3 se já não instalados.

```bash
apt install python3
apt install python3-pip
```

Clonar o repositório para a sua máquina local e acessar o repositório.

```bash
git clone https://github.com/PegasusAkira/http-cats_bot.git
cd http-cats_bot
```

E então usar o pip para instalar os requisitos do bot.

```bash
pip3 install -r requirements.txt
```

Modificar o arquivo core.py, adicionando suas credenciais da API do Twitter nas variáveis consumer_key, consumer_secret, access_token e access_token_secret.

E por último é só acessar a pasta do arquivo core.py e executar o bot.

```bash
cd src
python3 core.py
```

## Futuras atualizações:

- [X] Conseguir um seviço de hospedagem gratuito para o bot.
- [X] O Bot mostrar no terminal uma mensagem com a hora assim que uma mensagem for postada.
- [X] Criar um intervalo para o Bot não ficar repetindo uma imagem.
- [ ] Resolver problema de Timeout Error.
- [ ] Mensagem para o Bot responder alguém quando for marcado.
- [ ] Atualização de Status relativa a imagem a cada atualização.  
- [ ] Atualizar o Icon do Bot no Twitter.

Fotos retiradas do site [HTTP Cats](https://http.cat/)
