from flask import Flask
from app import sr
app = Flask(__name__)

# especifica una ruta para este servidor
@app.route('/') #decorador
def hello_world():
    return '<h1>hello, world</h1>'

@app.route('/articulos/')
def articulos():
    sr = sr()
    return sr.get_search()


# asignacion de una ruta dinamica
@app.route("/articulos/<id>")
def mostrar_articulo(id):
    return '<h1>vamos a mostrar el articulos con id: {}</h1>'.format(id)

#en caso de no encontrar la ruta devuelve esto
@app.errorhandler(404)
def page_not_found(error):
    return '<h1>Página no encontrada</h1>', 404

#esto se utiliza para poder correr la aplicaciòn en tiempo real.
#cuando ya este todo listo es mejor eliminarla
if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)