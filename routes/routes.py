from flask import Blueprint, jsonify, request
from services.services import obtenerPower, obtenerPuntos, actualizarPuntos, guardarTransaccion, obtenerTransacciones
from services.services import jalarImagen, obtenerRecompensas, obtenerPuntosMes, obtenerUltimaRecompensa
from services.services import crearUsuario, verifyUser

bp = Blueprint("reto", __name__)
@bp.route("/verifyUser/<string:correo>/<string:password>", methods=["GET"])
def verify_Usuario(Email: str, Pass:str):
    id = verificarUsuario(Email, Pass)
    return jsonify(id)

@bp.route("/insertUser", methods=["POST"])
def publishj_Usuario(Email: str, Pass:str):
    data = request.get_json()

    Email = data["idUser"]
    Pass = data["password"]
    Name = data["Name"]
    LastName = data["LastName"]
    id = crearUsuario(Email, Pass, Name, LastName)
    return jsonify(id)

@bp.route("/getpoints/<int:idUser>", methods=["GET"])
def get_puntos(idUser: int):
    puntos = obtenerPuntos(idUser)
    return jsonify(puntos)

@bp.route("/getpointsMes/<int:idUser>", methods=["GET"])
def get_puntosMes(idUser: int):
    puntos = obtenerPuntosMes(idUser)
    return jsonify(puntos)

#cambiamos <int:points> por <points> para que acepte cualquier caracter (incluyendo el signo -)
@bp.route("/updatepoints", methods=["PUT"])
def update_puntos():

    data = request.get_json()

    idUser = data["idUser"]
    points = data["points"]

    actualizarPuntos(idUser, points)

    return jsonify({"mensaje": "Puntos actualizados"})


@bp.route("/recompensas", methods=["GET"])
def get_recompensas():
    recompensas = obtenerRecompensas()
    return jsonify(recompensas)

@bp.route("/transaccion", methods=["POST"])
def post_transaccion():

    data = request.get_json()

    idUser = data["idUser"]
    idReward = data["idReward"]
    monto = data["monto"]
    description = data["description"]

    guardarTransaccion(idUser, idReward, monto, description)

    return jsonify({"mensaje": "Transacción guardada"})

@bp.route("/transacciones/<int:idUser>/<string:fechaBack>", methods=["GET"])
def get_transacciones(idUser: int, fechaBack: str):

    transacciones = obtenerTransacciones(idUser, fechaBack)
    return jsonify(transacciones)

@bp.route("/lastreward/<int:idUser>", methods=["GET"])
def get_last_reward(idUser: int):

    ultima_recompensa = obtenerUltimaRecompensa(idUser)

    return ultima_recompensa

@bp.route("/img/<int:id>", methods=["GET"])
def get_img(id: int):
    img = jalarImagen(id)
    return jsonify(img)

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    result = verifyUser(email, password)

    if result != 0:
        return jsonify(result)

    return jsonify(0), 401

@bp.route("/changeBg/<int:idBg>", methods=["GET"])
def change_bg(idBg: int):
    imageURL = changeBackground(idBg)
    return jsonify(imageURL)

@bp.route("/getPower", methods=["POST"])
def get_power():
    data = request.get_json()
    nombre = data["idUser"]

    power = obtenerPower(nombre)

    return jsonify(power)