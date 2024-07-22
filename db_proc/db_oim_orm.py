from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from sqlalchemy import VARCHAR, NVARCHAR, BIGINT, FLOAT, DOUBLE


Base = declarative_base()


class Manufacturers(Base):
    __tablename__ = 'Manufacturers'

    ID = Column(Integer(), primary_key=True)
    # maybe length 900
    ManufacturerName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)

    # Capacitors = relationship('Capacitors', backref='Manufacturers')
    # Resistors = relationship('Resistors', backref='Manufacturers')
    # Diods = relationship('Diods', backref='Manufacturers')
    # Microchips = relationship('Microchips', backref='Manufacturers')
    # Transistors = relationship('Transistors', backref='Manufacturers')


# class ComponentKinds(Base):
#     __tablename__ = 'ComponentKinds'
#
#
# class ComponentTypes(Base):
#     __tablename__ = 'ComponentKinds'
#
#
# class Technologies(Base):
#     __tablename__ = 'Technologies'
#
#
# class Diods(Base):
#     __tabblename__ = 'Diods'
#
#
# class Resistors(Base):
#     __tablename__ = 'Resistors'
#
#
# class Transistors(Base):
#     __tablename__ = 'Transistors'
#
#
# class Microchips(Base):
#     __tablename__ = 'Microchips'
#
#
class Capacitors(Base):
    __tablename__ = 'Capacitors'

    ID = Column(Integer(), primary_key=True)
    # DocID = Column(BIGINT(), nullable=True)
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False)

    # Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=True)
    # Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=True)
    # ManufacturerName_ID = Column(Integer(), ForeignKey('Manufacturers.ID'), nullable=True)

    OutputType = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)
    MinVoltage = Column(DOUBLE(), nullable=True)
    MaxVoltage = Column(FLOAT(), nullable=True)
    MinCapacity = Column(FLOAT(), nullable=True)
    MaxCapacity = Column(FLOAT(), nullable=True)
    MinOperatingTemperature = Column(FLOAT(), nullable=True)
    MaxOperatingTemperature = Column(FLOAT(), nullable=True)
    AcceptableCapacityIncrease = Column(FLOAT(), nullable=True)
    AcceptableСapacityReduction = Column(FLOAT(), nullable=True)
    # AcceptableCapacityReduction = Column(FLOAT(), nullable=True)
    QualicationSG = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)
    QualicationЕС = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)
    Remark1 = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)
    Remark2 = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)



def create_tables(engine):
    Base.metadata.create_all(engine)