import mysql.connector
from mysql.connector import Error

class BD():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'peliculas')
            print('Se ha conectado a la base datos')
        except Error as ex:
            print('La conexion ha tenido un error ', ex)
    def eliminar(self, sentencia):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(sentencia)
            except Error as ex:
                print('el ERROR al intentar la conexion es:',ex)
    def agregar(self, sentencia):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(sentencia)
            except Error as ex:
                print('el ERROR al intentar la conexion es:',ex)
    def select(self):
        if  self.conexion.is_connected():
            try:
                script = """
                    SELECT pelicula.id, pelicula.nombre_pelicula, genero.nombreg, pelicula.duracion, director.nombre FROM pelicula
                    INNER JOIN director on pelicula.id_director = director.id
                    INNER JOIN genero ON pelicula.id_genero = genero.id;           
                """
                cursor = self.conexion.cursor()
                cursor.execute(script)
                consulta = cursor.fetchall()
                return consulta
            except Error as ex: 
                print('el ERROR al intentar la conexion es:',ex)
base = BD()

consulta = BD().select()
print(consulta)
