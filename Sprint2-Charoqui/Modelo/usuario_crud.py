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


    def InsertarUsuario(self,rol,nombre,sexo,fecha,correo,telefono,DNI,contrasena):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSQL= "INSERT INTO usuario(idRol,nombre,sexo,fecha_nac,correo,telefono,DNI,contrasena) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
                data= (rol,nombre,sexo,fecha,correo,telefono,DNI,contrasena)

                cursor.execute(consultaSQL,data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print("No se pudo concectar a la base de datos")

    def BajaUsuario(self,ID):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM usuario WHERE idUsuario=%s;"
                cursor.execute(sentenciaSQL)

                self.conexion.commit()                
                self.conexion.close()
            except:
                print("No se pudo concectar a la base de datos")

    def ModificarUsuario(self,rol,nombre,sexo,fecha,correo,telefono,DNI,contrasena):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSQL= "UPDATE usuario SET idRol=%s,nombre=%s,sexo=%s,fecha_nac=%s,correo=%s,telefono=%s,DNI=%s,contrasena=%s where idUsuario;"
                data= (rol,nombre,sexo,fecha,correo,telefono,DNI,contrasena)

                cursor.execute(consultaSQL,data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print("No se pudo concectar a la base de datos")
    