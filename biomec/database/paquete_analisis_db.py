from ..models.entidades.Paquete_Analisis import Paquete_Analisis
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(paquete_analisis: Paquete_Analisis)->Paquete_Analisis:
    # comment: 
    sql = """"insert into Paquete_Analisis values(:ID, :Nombre)"""

    parametros = paquete_analisis._asdict()
    _fetch_none(sql,parametros)
    return paquete_analisis
# end def

def update(paquete_analisis: Paquete_Analisis)->Paquete_Analisis:
    sql = """"update Paquete_Analisis set ID=ID, Nombre=Nombre"""
    # comment: 
# end def

def delete(paquete_analisis: Paquete_Analisis)->Paquete_Analisis:
    # comment: 
    pass
# end def
def list_all():
    # comment: 
    sql = "SELECT * FROM Paquete_analisis ORDER BY ID DESC"
    print(sql)
    paqueteA_lista_sql = _fetch_all(sql,None)

    paquetes_lista = list(paqueteA_lista_sql)
    paqueteA_lista = []
    for x in range (len(paquetes_lista)):
        id_paqueteA  = paquetes_lista[x][0]
        nombre = paquetes_lista[x][1]
        #
        paquete_datos = {'ID':id_paqueteA, 'Nombre': nombre}
        #
        paqueteA_lista.append(paquete_datos)
    return paqueteA_lista
# end def