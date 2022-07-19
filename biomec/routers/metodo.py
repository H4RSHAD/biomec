from flask import Blueprint, flash, redirect, render_template, request, session, url_for


# importamos los controladores de Usuario
from ..controller import UserController

from ..controller import MetodoController
# importamos los Modelos 
from ..models.entidades.Metodo import Metodo

from ..routers.tipo import session # estoy importando la variable global donde se guarda la session del usuario que ingreso al sistema
metodo_scope = Blueprint('metodo',__name__)

#realizar la vista del Inicio o Home "template"
@metodo_scope.route('/', methods=['GET'])
def metodo():

    if session['Esta_logeado']:  # obtengo el dato de la session que se almaceno en la ruta tipo.login

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador",
                        "titulo": "Gestionar Metodo de analisi",
                       # "titulo_usuario":"Seguros Asociados al Laboratorio"
                }
 
        metodo_listar = MetodoController.list()    #! implementar el modelo seguro
        return render_template("usuario/admin/metodo.html", **parametros, items = metodo_listar)

    return redirect(url_for('tipo.login'))


@metodo_scope.route('/', methods=['GET'])
def metodo_recepcionista():

    if session['Esta_logeado']:  # obtengo el dato de la session que se almaceno en la ruta tipo.login

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Recepcionista",
                        "titulo": "Gestionar Metodo de analisis",
                       # "titulo_usuario":"Seguros Asociados al Laboratorio"
                }
 
        metodo_listar = MetodoController.list()    #! implementar el modelo seguro
        return render_template("usuario/personal/metodo.html", **parametros, items = metodo_listar)

    return redirect(url_for('tipo.login'))
    
