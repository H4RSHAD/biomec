from flask import Blueprint, flash, redirect, render_template, request, session, url_for


# importamos los controladores de Usuario
from ..controller import UserController

from ..controller import PrivilegioController
# importamos los Modelos 
from ..models.entidades.Privilegio import Privilegio

from ..routers.tipo import session # estoy importando la variable global donde se guarda la session del usuario que ingreso al sistema
privilegio_scope = Blueprint('privilegio',__name__)

#realizar la vista del Inicio o Home "template"
@privilegio_scope.route('/', methods=['GET'])
def privilegio():

    if session['Esta_logeado']:  # obtengo el dato de la session que se almaceno en la ruta tipo.login

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador",
                        "titulo": "Gestionar Seguro",
                        "titulo_usuario":"Seguros Asociados al Laboratorio"
                }
 
        cargo_lista = UserController.list()    #! implementar el modelo seguro
        return render_template("usuario/admin/privilegio.html", **parametros, items = cargo_lista)

    return redirect(url_for('tipo.login'))
