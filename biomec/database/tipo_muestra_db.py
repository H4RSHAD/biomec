from ..models.entidades.Tipo_Muestra import Tipo_Muestra
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(tipo_muestra: Tipo_Muestra)->Tipo_Muestra:
    # comment: 
    sql = """"insert into Tipo_Muestra values(:ID, :Nombre)"""

    parametros = tipo_muestra._asdict()
    _fetch_none(sql,parametros)
    return tipo_muestra
# end def

def update(tipo_muestra: Tipo_Muestra)-> Tipo_Muestra:
    sql = """"update Tipo_Muestra set ID = ID, Nombre=Nombre"""
    # comment: 
# end def

def delete(tipo_muestra: Tipo_Muestra)-> Tipo_Muestra:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT * FROM TipoMuestra ORDER BY ID DESC"
    print(sql)
    tipo_lista_sql = _fetch_all(sql,None)

    tipos_lista = list(tipo_lista_sql)
    tipo_lista = []
    for x in range (len(tipos_lista)):
        id_tipo  = tipos_lista[x][0]
        nombre = tipos_lista[x][1]
        #
        tipo_datos = {'ID':id_tipo, 'Nombre': nombre}
        #
        tipo_lista.append(tipo_datos)
    return tipo_lista
# end def