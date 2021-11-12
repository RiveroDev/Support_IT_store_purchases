

from flask import Flask

app = Flask(__name__)

@app.route("/compras")
def inicio():
    return " Hola"


if __name__=="__main__":

    app.run(host ='192.168.1.170',port=5000)






    
#"""
#app.run(host='0.0.0.0')
#ejemplo app.run(hot=<ip asignada a la pc> , port =<puerto asignado>)
#En el caso la pc la configuraciones host = '192.168.1.170' , port=5000 
#"""
