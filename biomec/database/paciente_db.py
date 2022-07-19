from ..models.entidades.Paciente import Paciente
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(paciente: Paciente)->Paciente:
    # comment: 
    sql = """"insert into Paciente values(:ID_Paciente, :Nro_Sg)"""

    parametros = paciente._asdict()
    _fetch_none(sql,parametros)
    return paciente
# end def

def update(paciente: Paciente)-> Paciente:
    sql = """"update Paciente set ID_Paciente = ID_Paciente, Nro_Sg=Nro_Sg"""
    # comment: 
# end def

def delete(paciente: Paciente)-> Paciente:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT paciente.id_paciente, persona.nombre, persona.apellidop, persona.apellidom, persona.telefono, persona.fecha_nacimiento, seguro.nombre_seguro FROM Paciente,Persona, Seguro where nro_sg = nro_seguro  and id_paciente = ci ORDER BY id_paciente DESC"
    print(sql)
    paciente_lista_sql = _fetch_all(sql,None)

    pacientes_lista = list(paciente_lista_sql)
    paciente_lista = []
    for x in range (len(pacientes_lista)):
        id_paciente  = pacientes_lista[x][0]
        nombre = pacientes_lista[x][1]
        apellidop = pacientes_lista[x][2]
        apellidom = pacientes_lista[x][3]
        telefono = pacientes_lista[x][4]
        fecha_nacimiento = pacientes_lista[x][5]
        nombre_seguro = pacientes_lista[x][6]
        #
        laboratorista_datos = {'ID_Paciente':id_paciente, 'Nombre': nombre, 'ApellidoP': apellidop, 'ApellidoM': apellidom, 'Telefono': telefono, 'Fecha_Nacimiento': fecha_nacimiento, 'Nombre_Seguro': nombre_seguro}
        #
        paciente_lista.append(laboratorista_datos)
    return paciente_lista