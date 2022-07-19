from ..models.entidades.Rol import Rol
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(rol: Rol)->Rol:
    # comment: 
    sql = """"insert into Rol values(:ID, :Nombre)"""

    parametros = rol._asdict()
    _fetch_none(sql,parametros)
    return rol
# end def

def update(rol: Rol)-> Rol:
    sql = """"update Rol set ID = ID, Nombre=Nombre"""
    # comment: 
# end def

def delete(rol: Rol)-> Rol:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT * FROM Rol ORDER BY ID DESC"
    print(sql)
    rol_lista_sql = _fetch_all(sql,None)

    roles_lista = list(rol_lista_sql)
    rol_lista = []
    for x in range (len(roles_lista)):
        id_rol  = roles_lista[x][0]
        nombre = roles_lista[x][1]
        #
        rol_datos = {'ID':id_rol, 'Nombre': nombre}
        #
        rol_lista.append(rol_datos)
    return rol_lista
# end def
