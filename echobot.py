import urllib
import json 
import requests
import time
from tokens import Tokens
from wit import Wit
import utils

TOKEN = Tokens().getTokens("PepeJuanProBot_telegram")
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
TOKENITO = 'ZQOLB3WQUZD734C4JEPJGUWDEMSWEBGE'

def send(request, response):
    print('Sending to user...', response['text'])
def my_action(request):
    print('Received from user...', request['text'])

actions = {
    'send': send,
    'my_action': my_action,
}



def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)    


def echo_all(updates, client):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            msg_witProperties = client.message(text)
            resp, moves, movement = utils.get_response(msg_witProperties)
            #resp = client.speech(open(resp, 'rb').read(), headers={'Content-Type': 'audio/wav'})['_text']
            print(resp)
            print("ya")
            #print(json.dumps(resp, indent=4, sort_keys=True))
            chat = update["message"]["chat"]["id"]
            send_message(resp, chat)
        except Exception as e:
            print("error")
            print(e)


def main():
    last_update_id = None
    client = Wit(access_token=TOKENITO)
    #Wit('TOKEN').speech(open('file.wav', 'rb').read(), headers={'Content-Type': 'audio/wav'})['_text']

    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates, client)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
