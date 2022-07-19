from ..models.entidades.Especialidad_Med import Especialida_Med
from ..database import especialidad_med_db

def create(especialidad_med: Especialida_Med)->Especialida_Med:
    # comment: 
    return especialidad_med_db.create(especialidad_med)


def update(especialidad_med: Especialida_Med)->Especialida_Med:
    # comment: 
    return especialidad_med_db.update(especialidad_med)


def delete(especialidad_med: Especialida_Med)->Especialida_Med:
    # comment: 
    return especialidad_med_db.delete(especialidad_med)


def list():
    return especialidad_med_db.list_all() 