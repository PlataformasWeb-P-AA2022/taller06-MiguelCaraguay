from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Fabrica, Sucursal

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad Club
sucursales = session.query(Sucursal).join(Fabrica).filter(Fabrica.tipo.like('comida')).order_by(Sucursal.numDepartamentos).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Sucursales")
for s in sucursales:
    print("%s" % (s))
    print("---------")












