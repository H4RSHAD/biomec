from ..models.entidades.Metodo import Metodo
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(metodo: Metodo)->Metodo:
    # comment: 
    sql = """"insert into metodo values(:ID, :Nombre)"""

    parametros = metodo._asdict()
    _fetch_none(sql,parametros)
    return metodo
# end def

def update(metodo: Metodo)->Metodo:
    sql = """"update metodo set ID = ID, Nombre=Nombre"""
    # comment: 
# end def

def delete(metodo: Metodo)->Metodo:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT * FROM Metodo ORDER BY ID DESC"
    print(sql)
    metodo_lista_sql = _fetch_all(sql,None)

    metodos_lista = list(metodo_lista_sql)
    metodo_lista = []
    for x in range (len(metodos_lista)):
        id_metodo  = metodos_lista[x][0]
        nombre = metodos_lista[x][1]
        #
        metodo_datos = {'ID':id_metodo, 'Nombre': nombre}
        #
        metodo_lista.append(metodo_datos)
    return metodo_lista
# end def