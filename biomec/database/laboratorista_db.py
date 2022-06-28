from ..models.entidades.Laboratorista import Laboratorista
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(laboratorista: Laboratorista)->Laboratorista:
    # comment: 
    sql = """"insert into Laboratorista values(:ID_Laboratorista, :ID_Esp_med)"""

    parametros = laboratorista._asdict()
    _fetch_none(sql,parametros)
    return laboratorista
# end def

def update(laboratorista: Laboratorista)-> Laboratorista:
    sql = """"update Laboratorista set ID_Laboratorista = ID_Laboratorista, ID_Esp_med=ID_Esp_med"""
    # comment: 
# end def

def delete(laboratorista: Laboratorista)-> Laboratorista:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT laboratorista.id_laboratorista, persona.nombre, persona.apellidop, persona.apellidom, persona.telefono, persona.fecha_nacimiento, especialida_med.nombre_esp FROM Laboratorista,Persona, Especialida_Med where id = id_esp_med  and id_laboratorista =ci ORDER BY ID_Laboratorista DESC"
    print(sql)
    laboratorista_lista_sql = _fetch_all(sql,None)

    laboratoristas_lista = list(laboratorista_lista_sql)
    laboratorista_lista = []
    for x in range (len(laboratoristas_lista)):
        id_laboratorista  = laboratoristas_lista[x][0]
        nombre = laboratoristas_lista[x][1]
        apellidop = laboratoristas_lista[x][2]
        apellidom = laboratoristas_lista[x][3]
        telefono = laboratoristas_lista[x][4]
        fecha_nacimiento = laboratoristas_lista[x][5]
        nombre_esp = laboratoristas_lista[x][6]
        #
        laboratorista_datos = {'ID_Laboratorista':id_laboratorista, 'Nombre': nombre, 'ApellidoP': apellidop, 'ApellidoM': apellidom, 'Telefono': telefono, 'Fecha_Nacimiento': fecha_nacimiento, 'Nombre_Esp': nombre_esp}
        #
        laboratorista_lista.append(laboratorista_datos)
    return laboratorista_lista