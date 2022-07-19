from ..models.entidades.Inventario import Inventario
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(inventario: Inventario)->Inventario:
    # comment: 
    sql = """"insert into inventario values(:ID, :Nombre, :Cantidad, :ID_lb)"""

    parametros = inventario._asdict()
    _fetch_none(sql,parametros)
    return inventario
# end def

def update(inventario: Inventario)->Inventario:
    sql = """"update inventario set ID = ID, Nombre=Nombre, ID_lb=ID_lb"""
    # comment: 
# end def

def delete(inventario: Inventario)->Inventario:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT inventario.id, inventario.nombre, inventario.cantidad, persona.nombre FROM Inventario,Laboratorista,Persona where id_lb = id_laboratorista  and id_laboratorista =ci ORDER BY ID DESC"
    print(sql)
    inventario_lista_sql = _fetch_all(sql,None)

    inventarios_lista = list(inventario_lista_sql)
    inventario_lista = []
    for x in range (len(inventarios_lista)):
        id_inventario  = inventarios_lista[x][0]
        nombre = inventarios_lista[x][1]
        cantidad = inventarios_lista[x][2]
        nombre_lab = inventarios_lista[x][3]
        #
        inventario_datos = {'ID':id_inventario, 'Nombre': nombre, 'Cantidad': cantidad, 'Nombre': nombre_lab}
        #
        inventario_lista.append(inventario_datos)
    return inventario_lista
# end def