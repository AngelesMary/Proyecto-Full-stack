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

    def InscribiraTorneo(self,usuario,nombreP,sexoP,fechaNacP,contactoP):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSQL= "INSERT INTO pareja_torneo(idUsuario,nombre_par,sexo_par,fecha_nac_par,contacto_par) VALUES(%s,%s,%s,%s,%s);"
                data= (usuario,nombreP,sexoP,fechaNacP,contactoP)

                cursor.execute(consultaSQL,data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print("No se pudo concectar a la base de datos")

    def BajaInscripcion(self,ID):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM pareja_torneo WHERE idPareja=%s;"
                cursor.execute(sentenciaSQL)

                self.conexion.commit()                
                self.conexion.close()
            except:
                print("No se pudo concectar a la base de datos")          