from flask import Blueprint, flash, redirect, render_template, request, session, url_for


# importamos los controladores de Usuario
from ..controller import UserController

from ..controller import PersonaController
from ..controller import LaboratoristaController
from ..controller import Especialidad_MedController
from ..controller import PrivilegioController

# importamos los Modelos 
from ..models.entidades.User import User 
from ..models.entidades.Persona import Persona 
from ..models.entidades.Laboratorista import Laboratorista
from ..models.entidades.Seguro import Seguro
from ..models.entidades.Especialidad_Med import Especialida_Med
from ..models.entidades.Privilegio import Privilegio

from ..routers.tipo import session # estoy importando la variable global donde se guarda la session del usuario que ingreso al sistema
especialidad_scope = Blueprint('especialista',__name__)

#realizar la vista del Inicio o Home "template"
@especialidad_scope.route('/', methods=['GET'])
def especialidad():

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
        return render_template("usuario/admin/especialidad.html", **parametros, items = cargo_lista)

    return redirect(url_for('tipo.login'))
