from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()


class Fabrica(Base):
    __tablename__ = 'fabrica'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100),nullable=False)
    direccion = Column(String(100),nullable=False)
    ciudad = Column(String(100), nullable=False)
    tipo = Column(String(100), nullable=False)

    sucursales = relationship("Sucursal", back_populates="fabrica")

    def __repr__(self):
        return "Fabrica: nombre=%s direccion=%s ciudad=%s tipo=%s" % (
                          self.nombre, 
                          self.direccion, 
                          self.ciudad,
                          self.tipo)

class Sucursal(Base):
    __tablename__ = 'sucursal'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    numEmpleados = Column(Integer)
    numDepartamentos = Column(Integer)
    volVentas = Column(Integer)

    fabrica_id = Column(Integer, ForeignKey('fabrica.id'))
  
    fabrica  = relationship("Fabrica", back_populates="sucursales")
    
    def __repr__(self):
        return "Sucursal: nombre: %s - numEmpleados %d -numDepartamentos:%d - volume de Ventas: %d" % (
                self.nombre, self.numEmpleados,self.numDepartamentos, self.volVentas)

Base.metadata.create_all(engine)









