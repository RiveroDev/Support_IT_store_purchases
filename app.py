
# inicio de flask 


from flask import Flask , render_template , request

app = Flask(__name__) #instancia de flask 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/comprobar_usuario",methods=['POST']) # recive las variables mandadas desde la ventana de incio
def usuario():  

    '''
    # ESTO ES CON EL METOSO GET---- SE USAR     request.args.get('nombre_de_la_variable')
    nombreUser = request.args.get('nameuser')
    passWord = request.args.get('password')
    '''
    passWord = request.form['password']
    nombreUser = request.form['userName']

    if nombreUser == 'richa' and int(passWord)==12345:
        return "<h1>Bienvenido " + nombreUser + "y  password: " + passWord + "</h1>"
    else:
        return "<h2> LA contraseña y clave son incorrectas </h2>"
            
@app.route("/<string:nombre>/")
def muestra_post(nombre):
    return f"Variasble con el nombre del post {nombre}"
    #return "Mostrar el pos {}".format(nombre)

@app.route("/reportes/")
def reportes():
    return render_template("reportes")

if __name__=="__main__":

    app.run(host='0.0.0.0',port =5500, debug= True)

#"""
#app.run(host='0.0.0.0')
#ejemplo app.run(hot=<ip asignada a la pc> , port =<puerto asignado>)
#En el caso la pc la configuraciones host = '192.168.1.170' , port=5000 
#"""
