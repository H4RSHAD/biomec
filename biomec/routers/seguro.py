from flask import Blueprint, flash, redirect, render_template, request, session, url_for


# importamos los controladores de Usuario
from ..controller import SeguroController
# importamos los Modelos 


from ..routers.tipo import session # estoy importando la variable global donde se guarda la session del usuario que ingreso al sistema
seguro_scope = Blueprint('seguro',__name__)

#realizar la vista del Inicio o Home "template"
@seguro_scope.route('/', methods=['GET'])
def seguro():

    if session['Esta_logeado']:  # obtengo el dato de la session que se almaceno en la ruta tipo.login

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador",
                        "titulo": "Gestionar Seguro",
                        "titulo_usuario":"Seguros Asociados al Laboratorio"
                }
        seguro_lista = SeguroController.list()
        #cargo_lista = UserController.list()    #! implementar el modelo seguro
        return render_template("usuario/admin/seguro.html", **parametros, items = seguro_lista)

    return redirect(url_for('tipo.login'))



#----------------------LOGIN------------------------------
@seguro_scope.route('/gestionar_seguro', methods=['GET','POST'])
def eliminar():
    if request.method == "GET":
        data = request.form   #guardo todos los datos ingresados por formulario de la vista
        print('----------- borrado SEGURO----------------------')
        print(data)
        print('-------------------------------------------------')        
        '''
        usuario = User(0,data['username'],data['password'],0,0)  # capturo los datos del formulario y mando al modelo User
                                                                 # los 0 son nulos porque no metemos desde formulario
        logged_user = UserController.login(usuario)
        
        if logged_user != None:         # Controlador de Usuario, si tienen datos
            print(str(logged_user.id_persona )+ ' id del usuario')
            if logged_user.password:    #si la contraseña coincide con el de la base de datos
                #return redirect(url_for('views.home')) # se dirigue a una "Dashborad", falta crearla

                session['Esta_logeado'] = True
                session['id_persona'] = logged_user.id_persona # id_persona del usuario
                session['id_rol'] = logged_user.id_rol #para comprobar su rol en las demas funciones               
                datos_de_persona = PersonaController.get_persona('CI',session['id_persona']) #para obtener su nombre completo
                #---concateno el nobre compleo despues de haber sacado los datos con el controlador de Persona
                session['username'] =  str(datos_de_persona.nombre) +" " +str(datos_de_persona.apellido_paterno)+" " +str(datos_de_persona.apellido_materno)



                # agregar aqui los numeros de roles para redirigir a su respectivo lugar
                lista_id_rol =[1,2,3]
                lista_tipo = ['tipo.roles','tipo.personal','tipo.tecnico'] 
                for id_rol in range(len(lista_id_rol)):
                        if logged_user.id_rol == lista_id_rol[id_rol]:
                                print('------datos de session para todos-------')
                                print("Usuario: " + session['username'] + " Tipo: " + str(session['id_rol']) )  
                                return redirect(url_for(lista_tipo[id_rol] )) #redirige dashboard que corresponde

            else:
                flash("Usuario o Contraseña invalida")           # Contraseña invalida
                return render_template('auth/login.html')
        else:
            flash("Usuario o Contraseña invalida")             # Usuario no encontrado
            return render_template('auth/login.html')
            '''
    else:
        return render_template('auth/login.html')

