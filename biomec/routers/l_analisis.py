from flask import Blueprint, flash, redirect, render_template, request, session, url_for


# importamos los controladores de Usuario
from ..controller import UserController

from ..controller import Lista_AnalisisController
# importamos los Modelos 
from ..models.entidades.Lista_Analisis import Lista_Analisis

from ..routers.tipo import session # estoy importando la variable global donde se guarda la session del usuario que ingreso al sistema
l_analisis_scope = Blueprint('l_analisis',__name__)

#realizar la vista del Inicio o Home "template"
@l_analisis_scope.route('/', methods=['GET'])
def analsisis():

    if session['Esta_logeado']:  # obtengo el dato de la session que se almaceno en la ruta tipo.login

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador",
                        "titulo": "Gestionar Lista de Analisis",
                       # "titulo_usuario":"Seguros Asociados al Laboratorio"
                }
 
        analisis_list = Lista_AnalisisController.list()   #! 
        return render_template("usuario/admin/lista_analisis.html", **parametros, items = analisis_list)

    return redirect(url_for('tipo.login'))


@l_analisis_scope.route('/', methods=['GET'])
def analsisis_recepcionista():

    if session['Esta_logeado']:  # obtengo el dato de la session que se almaceno en la ruta tipo.login

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Recepcionista",
                        "titulo": "Gestionar Lista de Analisis",
                       # "titulo_usuario":"Seguros Asociados al Laboratorio"
                }
 
        analisis_list = Lista_AnalisisController.list()   #! 
        return render_template("usuario/personal/lista_analisis.html", **parametros, items = analisis_list)

    return redirect(url_for('tipo.login'))