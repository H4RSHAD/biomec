from ..models.entidades.Metodo import Metodo
from ..database import metodo_db

def create(metodo: Metodo)->Metodo:
    # comment: 
    return metodo_db.create(metodo)
# end def

def update(metodo: Metodo)->Metodo:
    # comment: 
    return metodo_db.update(metodo)
# end def

def delete(metodo: Metodo)->Metodo:
    # comment: 
    return metodo_db.delete(metodo)
# end def
def list():
    # comment:
    return metodo_db.list_all() 
# end def