import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)#stado de http
    print(r.text)# informacion del http
    print(type(r.text))
    categories = r.json()#json lo transforma en una lista que reconoce python y se puede iterar
    for category in categories:
        print(category['name'])
'''
r.status_code <---- aquí hacemos una llamada al atributo del objeto

si queremos conocer todos los atributos con sus respectivos valores en un diccionario:

print(r.dict) o podemos usar el metodo vars print(vars(r))

tambien esta la funcion dir

print(dir(r)) <---- esta regresa todos los atributos del objeto sin los valores
'''