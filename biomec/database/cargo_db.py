from ..models.entidades.Cargo import Cargo
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(cargo: Cargo)->Cargo:
    # comment: 
    sql = """"insert into Cargo values(:ID_Cargo, :Nombre)"""

    parametros = cargo._asdict()
    _fetch_none(sql,parametros)
    return cargo
# end def

def update(cargo: Cargo)-> Cargo:
    sql = """"update Cargo set ID_Cargo = ID_Cargo, Nombre=Nombre"""
    # comment: 
# end def

def delete(cargo: Cargo)-> Cargo:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT * FROM Cargo ORDER BY ID_Cargo DESC"
    print(sql)
    cargo_lista_sql = _fetch_all(sql,None)

    cargos_lista = list(cargo_lista_sql)
    cargo_lista = []
    for x in range (len(cargos_lista)):
        id_cargo  = cargos_lista[x][0]
        nombre = cargos_lista[x][1]
        #
        cargo_datos = {'ID_Cargo':id_cargo, 'Nombre': nombre}
        #
        cargo_lista.append(cargo_datos)
    return cargo_lista
# end def