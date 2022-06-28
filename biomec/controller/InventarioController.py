from ..models.entidades.Inventario import Inventario
from ..database import inventario_db

def create(inventario: Inventario)->Inventario:
    # comment: 
    return inventario_db.create(inventario)
# end def

def update(inventario: Inventario)->Inventario:
    # comment: 
    return inventario_db.update(inventario)
# end def

def delete(inventario: Inventario)->Inventario:
    # comment: 
    return inventario_db.delete(inventario)
# end def