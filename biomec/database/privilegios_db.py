from ..models.entidades.Privilegio import Privilegio
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(privilegio: Privilegio)->Privilegio:
    # comment: 
    sql = """"insert into Laboratorista values(:ID_Laboratorista, :ID_Esp_med)"""

    parametros = privilegio._asdict()
    _fetch_none(sql,parametros)
    return privilegio
# end def

def update(laboratorista: Privilegio)-> Privilegio:
    sql = """"update Laboratorista set ID_Laboratorista = ID_Laboratorista, ID_Esp_med=ID_Esp_med"""
    # comment: 
# end def

def delete(laboratorista: Privilegio)-> Privilegio:
    # comment: 
    pass
# end def