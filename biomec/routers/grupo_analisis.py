from flask import Blueprint, flash, redirect, render_template, request, session, url_for


# importamos los controladores de Usuario
from ..controller import UserController

from ..controller import Paquete_AnalisisController
# importamos los Modelos 
from ..models.entidades.Paquete_Analisis import Paquete_Analisis

from ..routers.tipo import session # estoy importando la variable global donde se guarda la session del usuario que ingreso al sistema
g_analisis_scope = Blueprint('g_analisis',__name__)

#realizar la vista del Inicio o Home "template"
@g_analisis_scope.route('/', methods=['GET'])
def paquete_analisis():

    if session['Esta_logeado']:  # obtengo el dato de la session que se almaceno en la ruta tipo.login

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador",
                        "titulo": "Gestionar Grupo de Analisis",
                       # "titulo_usuario":"Seguros Asociados al Laboratorio"
                }
 
        g_analisis_lista = Paquete_AnalisisController.list()    #! implementar el modelo seguro
        return render_template("usuario/admin/grupo_analisis.html", **parametros, items = g_analisis_lista)

    return redirect(url_for('tipo.login'))
