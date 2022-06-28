from ..models.entidades.Especialidad_Med import Especialida_Med
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(especialidad_med: Especialida_Med)->Especialida_Med:
    # comment: 
    sql = """"insert into Especialida_Med values(:ID, :Nombre_Esp)"""

    parametros = especialidad_med._asdict()
    _fetch_none(sql,parametros)
    return especialidad_med
# end def

def update(especialidad_med: Especialida_Med)-> Especialida_Med:
    sql = """"update Especialida_Med set ID = ID, Nombre_Esp=Nombre_Esp"""
    # comment: 
# end def

def delete(especialidad_med: Especialida_Med)-> Especialida_Med:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT * FROM Especialida_Med ORDER BY ID DESC"
    print(sql)
    especialidad_lista_sql = _fetch_all(sql,None)

    especialidades_lista = list(especialidad_lista_sql)
    especialidad_lista = []
    for x in range (len(especialidades_lista)):
        id_especialidad  = especialidades_lista[x][0]
        Nombre_Esp = especialidades_lista[x][1]
        #
        especialidad_datos = {'ID':id_especialidad, 'Nombre_Esp': Nombre_Esp}
        #
        especialidad_lista.append(especialidad_datos)
    return especialidad_lista
# end def