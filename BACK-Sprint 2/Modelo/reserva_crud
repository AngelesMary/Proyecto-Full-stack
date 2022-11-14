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

    def ReservarCancha(self,usuario,cancha,fecha,estado):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSQL= "INSERT INTO reserva(idUsuario,numero_cancha,fecha_reserva,estado) VALUES(%s,%s,%s,%s);"
                data= (usuario,cancha,fecha,estado)

                cursor.execute(consultaSQL,data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print("No se pudo concectar a la base de datos")

    def ModificarReserva(self,usuario,cancha,fecha,estado):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSQL= "UPDATE reserva SET idUsuario=%s,numero_cancha=%s,fecha_reserva=%s,estado=%s WHERE idReserva=%s;"
                data= (usuario,cancha,fecha,estado)

                cursor.execute(consultaSQL,data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print("No se pudo concectar a la base de datos")