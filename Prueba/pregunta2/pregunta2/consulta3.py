from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_  

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
sucursales = session.query(Sucursal).join(Fabrica).filter(Fabrica.tipo.like('textiles')).all()
# Se recorre la lista a través de un ciclo
# repetitivo for en python
total = 0
for s in sucursales:
    total += s.numEmpleados
print("Numero total de empleados: ", total)






