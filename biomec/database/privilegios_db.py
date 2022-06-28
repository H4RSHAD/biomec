from ..models.entidades.Privilegio import Privilegio
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(privilegio: Privilegio)->Privilegio:
    # comment: 
    sql = """"insert into Privilegio values(:ID, :Descripcion)"""

    parametros = privilegio._asdict()
    _fetch_none(sql,parametros)
    return privilegio
# end def

def update(privilegio: Privilegio)-> Privilegio:
    sql = """"update Privilegio set ID = ID, Descripcion=Descripcion"""
    # comment: 
# end def

def delete(privilegio: Privilegio)-> Privilegio:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT * FROM Privilegio ORDER BY ID DESC"
    print(sql)
    privilegio_lista_sql = _fetch_all(sql,None)

    privilegios_lista = list(privilegio_lista_sql)
    privilegio_lista = []
    for x in range (len(privilegios_lista)):
        id_privilegio  = privilegios_lista[x][0]
        descripcion = privilegios_lista[x][1]
        #
        privilegio_datos = {'ID':id_privilegio, 'Descripcion': descripcion}
        #
        privilegio_lista.append(privilegio_datos)
    return privilegio_lista
# end def
