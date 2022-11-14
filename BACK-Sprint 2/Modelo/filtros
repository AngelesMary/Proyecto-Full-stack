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

    def BuscarCancha(self,parametro):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSQL= "SELECT * FROM cancha WHERE iluminacion= %s;"
                cursor.execute(consultaSQL)
                resultado = cursor.fetchall()
                self.conexion.close()
                return resultado

            except:
                print("No se pudo concectar a la base de datos")

    def BuscarTurno(self,fecha):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSQL= "SELECT numero_cancha, T1,T2,T3 FROM turno as t INNER JOIN cancha as c ON t.numero_cancha=c.numero_cancha where t.fecha=%s and T1=%s || T2=%s|| T3=%s;"
                cursor.execute(consultaSQL)
                resultado = cursor.fetchall()
                self.conexion.close()
                return resultado

            except:
                print("No se pudo concectar a la base de datos")

    def BuscarTorneo(self,fecha):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSQL= "SELECT * FROM torneo WHERE fecha= %s;"
                cursor.execute(consultaSQL)
                resultado = cursor.fetchall()
                self.conexion.close()
                return resultado

            except:
                print("No se pudo concectar a la base de datos")