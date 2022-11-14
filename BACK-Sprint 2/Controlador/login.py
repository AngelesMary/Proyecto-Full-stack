import mysql.connector

try:
	conexion = mysql.connector.connect(
    user="root",password="root",host="localhost",
    database="bd_club_prueba",port="3306"
)
	try:
		with conexion.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
			cursor.execute("SELECT * FROM turno;")
 
			# Con fetchall traemos todas las filas
			Turnos = cursor.fetchall()
 
			# Recorrer e imprimir
			for turn  in Turnos:
				print(turn)
	finally:
		conexion.close()
	
except (mysql.err.OperationalError, mysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)