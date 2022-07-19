from flask import Blueprint, flash, redirect, render_template, request, session, url_for


# importamos los controladores de Usuario
from ..controller import UserController

from ..controller import LaboratoristaController
# importamos los Modelos 
from ..models.entidades.Laboratorista import Laboratorista

from ..routers.tipo import session # estoy importando la variable global donde se guarda la session del usuario que ingreso al sistema
laboratorista_scope = Blueprint('laboratorista',__name__)

#realizar la vista del Inicio o Home "template"
@laboratorista_scope.route('/', methods=['GET'])
def laboratorista():

    if session['Esta_logeado']:  # obtengo el dato de la session que se almaceno en la ruta tipo.login

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador",
                        "titulo": "Gestionar Medico",
                        "titulo_usuario":"Seguros Asociados al Laboratorio"
                }
 
        cargo_lista = LaboratoristaController.list()    #! implementar el modelo seguro
        return render_template("usuario/admin/laboratorista.html", **parametros, items = cargo_lista)

    return redirect(url_for('tipo.login'))
