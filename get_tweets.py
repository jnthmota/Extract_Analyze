import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

# Cadastrar as chaves de acesso
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

# Definindo um arquivo de saída para armazenar os tweets coletados
data_hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open (f"collect_tweets_{data_hoje}.txt", "w")
#out = open ("collect_tweets.txt", "w") Armazenando e dando overwrite nos dados caso exista

# Implementar uma classe para conexão com o Twitter
#Herança 
#Classe MyListener vai extender o StreamListener
class MyListener(StreamListener):

    def on_data(self, data):
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True

    def on_error(self, status):
        print(status)

# Implementar a nossa função MAIN
if __name__ == '__main__':
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track = ["Vacinas"])
