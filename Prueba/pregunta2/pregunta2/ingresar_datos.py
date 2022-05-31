from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

empresas = []
with open ('data/empreas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for linea in archivo:
        linea = linea.split('|')
        empresa = Fabrica(nombre = linea[0],direccion = linea[1],ciudad=  linea[2], tipo= linea[3].replace('\n',''))
        session.add(empresa)



session.commit()

with open ('data/sucursales.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for linea in archivo:
        linea = linea.split('|')
        fabric = session.query(Fabrica).filter_by(nombre=linea[1]).one()
        empresa = Sucursal(nombre = linea[0],numEmpleados= linea[2], numDepartamentos=linea[3], volVentas=linea[4].replace('\n',''), fabrica = fabric   )
        session.add(empresa)

session.commit()
