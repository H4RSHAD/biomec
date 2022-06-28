from ..models.entidades.Lista_Analisis import Lista_Analisis
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(lista_analisis: Lista_Analisis)->Lista_Analisis:
    # comment: 
    sql = """"insert into Lista_Analisis values(:ID, :Nombre, :Precio, :ID_Pqa)"""

    parametros = lista_analisis._asdict()
    _fetch_none(sql,parametros)
    return lista_analisis
# end def

def update(lista_analisis: Lista_Analisis)->Lista_Analisis:
    sql = """"update Lista_Analisis set ID=ID, Nombre=Nombre, Precio=Precio, ID_Pqa=ID_Pqa"""
    # comment: 
# end def

def delete(lista_analisis: Lista_Analisis)->Lista_Analisis:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT L_Analisis.id, L_Analisis.nombre, L_Analisis.precio FROM L_AnalisisORDER BY ID DESC"
    print(sql)
    l_analisis_lista_sql = _fetch_all(sql,None)

    analisis_lista = list(l_analisis_lista_sql)
    analisis_lista = []
    for x in range (len(analisis_lista)):
        id_analisis  = analisis_lista[x][0]
        nombre = analisis_lista[x][1]
        precio = analisis_lista[x][2]

        #
        seguro_datos = {'ID':id_analisis, 'Nombre': nombre, 'Nombre': precio}
        #
        analisis_lista.append(seguro_datos)
    return analisis_lista
# end def