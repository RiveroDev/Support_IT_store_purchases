

from flask import Flask

app = Flask(__name__)

@app.route("/compras")
def compras():
    return "<h1><p>Hola esto es una prueba de red  'Hola Caro'</p></h1>"


@app.route("/")
def index():
    return "<p>Pagina de inicio</p>"


@app.route("/<string:nombre>/")
def muestra_post(nombre):
    return f"Variasble con el nombre del post {nombre}"
    #return "Mostrar el pos {}".format(nombre)

if __name__=="__main__":

    app.run(host ='192.168.1.170', port =5500)

#"""
#app.run(host='0.0.0.0')
#ejemplo app.run(hot=<ip asignada a la pc> , port =<puerto asignado>)
#En el caso la pc la configuraciones host = '192.168.1.170' , port=5000 
#"""
