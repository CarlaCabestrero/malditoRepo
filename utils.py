


def wit_response(message_text):
    resp = client.message(message_text)
    categories = {'adjetives': None, 'category': None}

    entities = list(resp['entities'])

    for entity in entities:
        categories[entity] = resp['entities'][entity][0]['value']

    return categories


# print(wit_response(wit_response("I want nice puppies pics")))

def get_response(msg):
    resp = handle_message(msg)

    return resp


def handle_message(response):
    entities = response['entities']
    print("a")
    media = first_entity_value(entities, 'media')
    category = first_entity_value(entities, 'category')
    adjetive = first_entity_value(entities, 'adjetive')
    moves = False
    movement = None
º
    if category:
        if adjetive and media:
            pepe = 'Here there go some {} {} {}.'.format(adjetive, category, media)
        elif adjetive:
            pepe = 'Here there go some {} {}.'.format(adjetive, category)
        elif media:
            pepe = 'Here there go some {} {}.'.format(category, media)
        else:
            pepe = 'Here there go some {}.'.format(category)
        return pepe


# We can call the wikidata API using the wikidata ID for more info


#     return wikidata_description(celebrity)
# elif greetings:
#     return 'Hi! You can say a category"'
# else:
#     return "Um. Sorry, I don't understand. "

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val


def categories(message_text):
    resp = client.message(message_text)
    categories = {'newstype': None, 'location': None}

    entities = list(resp['entities'])

    for entity in entities:
        categories[entity] = resp['entities'][entity][0]['value']

    return categories


def get_news_elements(categories):
    news_client = gnewsclient()
    news_client.query = ''

    if categories['location'] != None:
        news_client.query += categories['location']

    if categories['newstype'] != None:
        news_client.query += categories['newstype'] + ' '

    news_items = news_client.get_news()
    elements = []

    for item in news_items:
        element = {
            'title': item['title'],
            'buttons': [{
                'type': 'web_url',
                'title': "Read more",
                'url': item['link']
            }],
            'image_url': item['img']
        }
        elements.append(element)

    return elements


# print(get_news_elements(wit_response("I want sports news in India")))
# text = {'_text': 'please send me cat pics',
#         'entities': {'category': [{'confidence': 0.963340171631, 'value': 'cat', 'type': 'value'}],
#                      'media': [{'confidence': 0.97895949703172, 'value': 'pics', 'type': 'value'}]},
#         'msg_id': '0GBe2KgmT6Oope0WE'}

#get_response(text)
