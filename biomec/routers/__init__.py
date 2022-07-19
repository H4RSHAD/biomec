#Aqui centralizamos todos los blueprint, que se importaran al archivo  => __init__.py principal,de la carpeta biomec
#Es un atajo

from .tipo import tipo_scope #rutas del login 
from .routers import global_scope #rutas el inicio

from .seguro import seguro_scope #rutas del seguro
from .personal import personal_scope #ruta del personal del laboratorio
from .laboratorista import laboratorista_scope
from .especialidad import especialidad_scope
from .privilegio import privilegio_scope
from .paciente import paciente_scope
from .grupo_analisis import g_analisis_scope
from .metodo import metodo_scope
from .l_analisis import l_analisis_scope