from ..models.entidades.Privilegio_Rol import Privilegio_Rol
from ..database import privilegios_rol_db

def create(privilegio_rol: Privilegio_Rol)->Privilegio_Rol:
    # comment: 
    return privilegios_rol_db.create(privilegio_rol)
# end def

def update(privilegio_rol: Privilegio_Rol)->Privilegio_Rol:
    # comment: 
    return privilegios_rol_db.update(privilegio_rol)
# end def

def delete(privilegio_rol: Privilegio_Rol)->Privilegio_Rol:
    # comment: 
    return privilegios_rol_db.delete(privilegio_rol)
# end def
def list():
    # comment:
    return privilegios_rol_db.list_all()
# end def