import sys
from wit import Wit
from tokens import Tokens

TOKEN = Tokens().getTokens("PepeJuanProBot_telegram")
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def send(request, response):
    print(response['text'])


def reply_all(request):

    # Reply filling all its variables
    context = request['context']
    print("hi")
    entities = request['entities']
    print("hola")
    for k in entities.keys():
        k = str(k)
        context[k] = str(entities[k][0]['value'])

    return context

if __name__ == "__main__":

    # You can either pass a token as an argument or not (default)
    if len(sys.argv) != 2:
        print('***** Using default token *****')
        access_token = TOKEN
    else:
        access_token = sys.argv[1]

    actions = {
        'send': send,
        'reply_all': reply_all,
    }

    client = Wit(access_token=access_token)
client.interactive() 
