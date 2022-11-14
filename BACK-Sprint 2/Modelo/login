import mysql.connector

class Conexion():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'root',
                db = 'db_padle'
            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)


    def Login(self,DNI,contrasena):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSQL= "SELECT * FROM usuario where DNI=%s and contrasena=%s;"
                cursor.execute(consultaSQL)
                resultado = cursor.fetchall()
                self.conexion.close()
                return resultado

            except:
                print("No se pudo concectar a la base de datos")