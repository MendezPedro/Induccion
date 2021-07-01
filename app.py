import xmlrpc.client

#configuration
url = 'http://52.142.63.20:1269'
db = 'fraccion_test'
username = 'WSadnet@adnetworks.cl'
password = 'WSadnet@adnetworks.cl'


#logging
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

uid = common.authenticate(db, username, password, {})

#calling methods for "execute_kw"
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False})

#search_count
search_count = models.execute_kw(db, uid, password,
    'res.partner', 'search_count',
    [[['is_company', '=', True], ['customer', '=', True]]])

print(search_count)

#search and read
search_read = models.execute_kw(db, uid, password,
    'res.partner', 'search_read',
    [[['is_company', '=', True], ['customer', '=', True]]],
    {'fields': ['name', 'country_id', 'comment'], 'limit': 5})


#devuelve llaves en español
lista = []
for element in search_read:
    dicc = {}
    dicc['id'] = element['id']
    dicc['nombre'] = element['name']
    dicc['pais_id'] = element['country_id']
    dicc['comentarios'] = element['comment']
    lista.append(dicc)

print(lista)




