from ..models.entidades.Personal import Personal
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none, _fetch_one

def create(personal: Personal)->Personal:
    # comment: 
    sql = """"insert into Personal values(:ID_Persona, :ID_Crg)"""

    parametros = personal._asdict()
    _fetch_none(sql,parametros)
    return personal
# end def

def update(personal: Personal)-> Personal:
    sql = """"update Personal set ID_Persona = ID_Persona, ID_Crg=ID_Crg"""
    # comment: 
# end def

def delete(personal: Personal)-> Personal:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT personal.id_persona, persona.nombre, persona.apellidop, persona.apellidom, persona.telefono, persona.fecha_nacimiento, cargo.nombre FROM Personal,Persona, Cargo where id_cargo = id_crg  and id_persona =ci ORDER BY ID_Persona DESC"
    print(sql)
    personal_lista_sql = _fetch_all(sql,None)

    personales_lista = list(personal_lista_sql)
    personal_lista = []
    for x in range (len(personales_lista)):
        id_personal  = personales_lista[x][0]
        nombre = personales_lista[x][1]
        apellidop = personales_lista[x][2]
        apellidom = personales_lista[x][3]
        telefono = personales_lista[x][4]
        fecha_nacimiento = personales_lista[x][5]
        nombre_cargo = personales_lista[x][6]
        #
        personal_datos = {'ID_Personal':id_personal, 'Nombre': nombre, 'ApellidoP': apellidop, 'ApellidoM': apellidom, 'Telefono': telefono, 'Fecha_Nacimiento': fecha_nacimiento, 'Nombre_Cargo': nombre_cargo}
        #
        personal_lista.append(personal_datos)
    return personal_lista