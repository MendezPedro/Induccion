import xmlrpc.client

url = 'http://52.142.63.20:1269'
db = 'fraccion_test'
username = 'WSadnet@adnetworks.cl'
password = 'WSadnet@adnetworks.cl'

class consulta():

    def __init__(self):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        print(url)

    def logging(self):

        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        common.version()
        uid = common.authenticate(db, username, password, {})
        return uid

    def models_id(self):
        
        usuario_id = information.logging()
        
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        models.execute_kw(db, usuario_id, password,
            'res.partner', 'check_access_rights',
            ['read'], {'raise_exception': False})
        return models
        

    def search_count(self):
        
        uid = information.logging()
        models = information.models_id()

        s_count = models.execute_kw(db, uid, password,
            'res.partner', 'search_count',
            [[['is_company', '=', True], ['customer', '=', True]]])
        return s_count


    def search_read(self):
        uid = information.logging()
        models = information.models_id()
        
        s_read = models.execute_kw(db, uid, password,
            'res.partner', 'search_read',
            [[['is_company', '=', True], ['customer', '=', True]]],
            {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
        return s_read


information = consulta()
print("imprime search count: ", information.search_count())

search_read = information.search_read()
print("imprime search read: ", search_read)

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




