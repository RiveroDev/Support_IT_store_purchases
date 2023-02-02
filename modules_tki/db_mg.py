import sqlite3 as db
import datosOP as Op


def conexion_base_de_datos(name_db:str) -> object: 
    try:
        BD = db.connect(name_db)
    except db.OperationalError as error:
        print("Error de conexcion")
    return BD

def comando_SQL(slq_comand: dict):   

    BD = conexion_base_de_datos(nan) # instanci y conexion a la base de datos 
    cursor = BD.cursor()
    tabla = slq_comand
    for row in tabla:
        cursor.execute(row)          #ejecuta la condicion para la creacion de cada columna 

def insertar_bd():
    pass

try:
	bd = sqlite3.connect("libros.db")   #-------------> analizar esta operacion 
	cursor = bd.cursor()
	libros = [
		"""
		INSERT INTO libros
		(autor, genero, precio, titulo)
		VALUES
		('Stephen King', 'Terror', 115,'Cementerio de animales'),
		('Alfred Bester', 'Ciencia ficción', 200,'Las estrellas, mi destino'),
		('Margaret Atwood', 'Ciencia ficción', 150,'El cuento de la criada');
		"""
	]
	for sentencia in libros:
		cursor.execute(sentencia);
	bd.commit() #Guardamos los cambios al terminar el ciclo
	print("Libros insertados correctamente")
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)

#   este parte es lo mismo pero insertando datos

try:
	bd = sqlite3.connect("libros.db")
	cursor = bd.cursor()
	autor = input("\nAutor: ")
	genero = input("\nGénero: ")
	precio = float(input("\nPrecio: "))
	titulo = input("\nTítulo: ")
	sentencia = "INSERT INTO libros(autor, genero, precio, titulo) VALUES (?,?,?,?)"
	cursor.execute(sentencia, [autor, genero, precio, titulo])
	bd.commit()
	print("Guardado correctamente")
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)

def 

nan = Op.name_DB   # buscamos el nombre de la base de datos
conexion_base_de_datos(nan) #ejemplo de conexion  data.db va a ser el nombre de la base de datos

tab = Op.tablas   # variable global
comando_SQL(tab)