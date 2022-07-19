from ..models.entidades.Paciente import Paciente
from ..database import paciente_db

def create(paciente: Paciente)->Paciente:
    # comment: 
    return paciente_db.create(paciente)
# end def

def update(paciente: Paciente)->Paciente:
    # comment: 
    return paciente_db.update(paciente)
# end def

def delete(paciente: Paciente)->Paciente:
    # comment: 
    return paciente_db.delete(paciente)
# end def
def list():
    # comment:
    return paciente_db.list_all()
# end def