request1 = {
    'category_id': 1,
    'label': 'text',
    'xuy': 'chlen',
    'pizda': 'vagina'
}
request2 = {
    'category_id': 1,
    'label': 'text',
}
request3 = {
    'category_id': 1,
    'label': 'text',
    'pizda': 'vagina'
}


def MySQL(req):
    print(f'''INSERT INTO table ({', '.join([str(f"'{i}'") for i in req.keys()])}) VALUES ({', '.join([str(f"'{i}'") for i in req.values()])});''')
    return req
a = MySQL(request2)
