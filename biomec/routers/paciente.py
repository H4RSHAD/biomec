from flask import Blueprint, flash, redirect, render_template, request, session, url_for


# importamos los controladores de Usuario
from ..controller import UserController
from ..controller import PersonaController
from ..controller import LaboratoristaController
from ..controller import PacienteController
# importamos los Modelos 
from ..models.entidades.User import User 
from ..models.entidades.Persona import Persona 
from ..models.entidades.Laboratorista import Laboratorista
from ..models.entidades.Paciente import Paciente

from ..routers.tipo import session # estoy importando la variable global donde se guarda la session del usuario que ingreso al sistema
paciente_scope = Blueprint('paciente',__name__)

#realizar la vista del Inicio o Home "template"
@paciente_scope.route('/', methods=['GET'])
def paciente():

    if session['Esta_logeado']:  # obtengo el dato de la session que se almaceno en la ruta tipo.login

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador",
                        "titulo": "Gestionar Paciente",
                        "titulo_usuario":"Listado del personal de la Empresa"
                }
 
        personas_lista = PacienteController.list()    #! implementar el modelo personal
        print(personas_lista)
        return render_template("usuario/admin/paciente.html", **parametros, items = personas_lista)

    return redirect(url_for('tipo.login'))
