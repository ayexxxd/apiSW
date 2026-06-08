from bd import get_db_connection
from datetime import date
from flask import jsonify

def crearUsuario(Email: str, Password: str, Name: str, LastName:str):
    conexion = get_db_connection
    cursor = conexion.cursor()

    query = "insert into Usuarios values(%s,%s,%s,%s,CURDATE(),0,0,0)"

    cursor.execute(query,(Name, LastName,Email,Password))

    conexion.commit()

    cursor.close()
    conexion.close()

def obtenerPuntos(idUser: int):
    conexion = get_db_connection()
    cursor = conexion.cursor()

    query = "select whirltokens from Usuarios where idusuario = %s;"
    
    cursor.execute(query, (idUser,))

    puntos = cursor.fetchone()[0]

    cursor.close()
    conexion.close()

    return puntos


def obtenerPuntosMes(idUser: int):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    query = ( "select coalesce(sum(monto),0) as puntos from Transacciones "
        "where idusuario = %s and fecha >= now() - interval 1 month "
        "and monto > 0;"
    )

    cursor.execute(query, (idUser,))

    puntos = cursor.fetchone()

    cursor.close()
    conexion.close()

    return int(puntos["puntos"])


def actualizarPuntos(idUser: int, points: int):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    query = (
        "update Usuarios set whirltokens = whirltokens + %s where idusuario = %s;"
    )

    cursor.execute(query, (points, idUser))

    conexion.commit()

    cursor.close()
    conexion.close()

    return 0


def obtenerRecompensas():
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    query = "select * from Recompensas;"

    cursor.execute(query)

    recompensas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return recompensas


def guardarTransaccion(
    idUser: int,
    idReward: int,
    monto: int,
    description: str
):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    query = ("insert into Transacciones (idusuario, idrecompensa, monto, fecha, descripcion) "
        "values (%s, %s, %s, curdate(), %s);"
    )

    cursor.execute(query,(idUser, idReward, monto, description))

    conexion.commit()

    cursor.close()
    conexion.close()

    return {"mensaje": "transacción guardada"}


def obtenerTransacciones(
    idUser: int,
    fechaBack: str = None
):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    fechaCurrent = date.today().strftime("%Y-%m-%d")

    if fechaBack is None:

        query = ("select * from Transacciones where idusuario = %s "
            "order by fecha desc;")

        cursor.execute(query, (idUser,))

    else:
        query = ("select * from Transacciones where idusuario = %s "
            "and date(fecha) >= %s and date(fecha) <= %s "
            "order by fecha desc;"
        )

        cursor.execute(query,(idUser, fechaBack, fechaCurrent))

    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados


def obtenerUltimaRecompensa(idUser: int):
    conexion = get_db_connection()
    cursor = conexion.cursor()

    query = ("SELECT Descripcion FROM Transacciones WHERE IdUsuario = %s AND Monto < 0 ORDER BY Fecha DESC, IdTransaccion DESC LIMIT 1;"
    )

    cursor.execute(query, (idUser,))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if resultado is None:
        return "Sin canjes recientes"

    return resultado[0]


def jalarImagen(id: int):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    query = ("select nombre, imagen from Minijuegos where idjuego = %s;")

    cursor.execute(query, (id,))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado


def verifyUser(email: str, password: str):
    conexion = get_db_connection()
    cursor = conexion.cursor()

    query = "SELECT IdUsuario FROM Usuarios WHERE Correo = %s AND Contrasena = %s;"

    cursor.execute(query, (email, password))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()


    if resultado is None:
        return 0
    else:
        return resultado[0]
    
def obtenerPower(powerName: str):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    query = "SELECT Velocidad, Daño, Espera FROM PoderesCazador where Nombre = %s;"

    cursor.execute(query, (powerName,))

    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultado