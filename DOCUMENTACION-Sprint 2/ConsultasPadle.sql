--  CONSULTAS

-- Cancha
use bd_padle;
INSERT INTO cancha(superficie,iluminacion,techado,direccion,imagen,costo) VALUES("%s","%s","%s","%s","%s","%s");
UPDATE cancha SET superficie="%s",iluminacion="%s",techado="%s",direccion="%s",imagen="%s",costo="%s" where numero_cancha= "%s";
DELETE FROM cancha WHERE numero_cancha= "%s";
SELECT * FROM cancha WHERE iluminacion= "%s";

--  Opinion
use bd_padle;
INSERT INTO opinion(idUsuario,puntuacion,comentario) VALUES("%s","%s","%s");
DELETE FROM opinion WHERE idOpinion="%s";
SELECT comentario,puntuacion FROM opinion WHERE puntuacion<5;

--  Pareja_torneo
use bd_padle;
INSERT INTO pareja_torneo(idUsuario,nombre_par,sexo_par,fecha_nac_par,contacto_par) VALUES("%s","%s","%s","%s","%s");
DELETE FROM pareja_torneo WHERE idPareja="%s";
SELECT * FROM pareja_torneo;

--  Reserva
use bd_padle;
INSERT INTO reserva(idUsuario,numero_cancha,fecha_reserva,estado) VALUES("%s","%s","%s","%s");
UPDATE reserva SET idUsuario="%s",numero_cancha="%s",fecha_reserva="%s",estado="%s" WHERE idReserva="%s";
SELECT * FROM reserva where idUsuario="%s";

-- Rol
use bd_padle;
INSERT INTO rol(rol) VALUES ("%s");

-- Torneo
use bd_padle;
INSERT INTO torneo(nombre_tor,fecha,direccion) VALUES("%s","%s","%s");
UPDATE toneo SET nombre_tor="%s",fecha="%s",direccion="%s" WHERE idTorneo="%s";
SELECT * FROM torneo WHERE fecha="%s";

-- Turno
use bd_padle;
INSERT INTO turno(numero_cancha,fecha,T1,T2,T3) VALUES("%s","%s","%s","%s","%s");
UPDATE turno SET numero_cancha="%s",fecha="%s",T1="%s",T2="%s",T3="%s" WHERE idTurno="%s";
SELECT numero_cancha, T1,T2,T3 FROM turno as t INNER JOIN cancha as c ON t.numero_cancha=c.numero_cancha where t.fecha="%s" and T1="%s" || T2="%s"|| T3="%s";

-- Usuario
use bd_padle;
INSERT INTO usuario(idRol,nombre,sexo,fecha_nac,correo,telefono,DNI,contrasena) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s");
UPDATE usuario SET idRol="%s",nombre="%s",sexo="%s",fecha_nac="%s",correo="%s",telefono="%s",DNI="%s",contrasena="%s" where idUsuario="%s";
DELETE FROM usuario WHERE idUsuario="%s";
SELECT * FROM usuario where DNI="%s" and contrasena="%s";


 


