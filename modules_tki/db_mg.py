import sqlite3 as db



def conexion_base_de_datos(name_db:str) -> object: 
    try:
        BD = db.connect(name_db)
    except db.OperationalError as error:
        print("Error de conexcion")
    return BD

def comando_SQL(slq_comand: str):   

    BD = conexion_base_de_datos(name_db) # instanci y conexion a la base de datos 
    BD.cursor(slq_comand)



#conexion_base_de_datos("data.db") ejemplo de conexion  data.db va a ser el nombre de la base de datos