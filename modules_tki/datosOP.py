


name_DB = "data.db"  # ruta y nombre de la base de datos


# El comando es crear una tabla si no exites con las columnas autor, genero ,precio, titulo
tablas = [
		"""
			CREATE TABLE IF NOT EXISTS libros(
				autor TEXT NOT NULL,
				genero TEXT NOT NULL,
				precio REAL NOT NULL,
				titulo REAL NOT NULL
			);
		"""
	]