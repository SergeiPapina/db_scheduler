from db_connect import get_connection_mssql
from sqlalchemy.orm import sessionmaker
from db_insert_data import *
from db_get_data import get_all
from db_oim_orm import (Manufacturers, Capacitors, ComponentKinds, ComponentTypes,
                        Technologies, Resistors, Diods, Transistors, Microchips)


if __name__ == '__main__':
    engine = get_connection_mssql()

    Session = sessionmaker(bind=engine)
    session = Session()

    manufacturers = get_all(session, Manufacturers)
    for _ in manufacturers:
        print(_.ID, _.ManufacturerName, len(_.Capacitors), len(_.Resistors), len(_.Diods), len(_.Transistors))

    kinds = get_all(session, ComponentKinds)
    for _ in kinds:
        print(_.ID, _.RuComponentKind, _.EnComponentKind)

    kinds = get_all(session, ComponentTypes)
    for _ in kinds:
        print(_.ID, _.RuComponentType, _.EnComponentType)

    resistors = get_all(session, Resistors)
    for _ in resistors:
        print(_.ID)

    diodes = get_all(session, Diods)
    for _ in diodes:
        print(_.ID, _.DocID, _.ComponentName, _.Type_ID, _.Kind_ID, _.ManufacturerName_ID, _.MaxPermissibleDCVoltage,
              _.MinOperatingTemperature, _.MaxOperatingTemperature, _.MaxPermissibleAverageDirectCurrent,
              _.MaxiPermissibleDirectCurrent, _.RadiationResistance, _.RadiationResistanceI, _.QualicationSG,
              _.QualicationЕС, _.Package, _.Remark1, _.Remark2)

    technologies = get_all(session, Technologies)
    for _ in technologies:
        print(_.ID, _.RuTechnologyName, _.EnTechnologyName)

    capacitors = get_all(session, Capacitors)
    for _ in capacitors:
        print(_.ID, _.Type_ID, _.DocID, _.Kind_ID, _.ComponentName, _.ManufacturerName_ID, _.OutputType, _.MinVoltage,
              _.MaxVoltage,
              _.MinCapacity, _.MaxCapacity,
              _.MinOperatingTemperature, _.MaxOperatingTemperature, _.AcceptableCapacityIncrease,
              _.AcceptableСapacityReduction, _.QualicationSG, _.QualicationЕС, _.Remark1, _.Remark2)

    transistors = get_all(session, Transistors)
    for _ in transistors:
        print(_.ID, _.DocID, _.ComponentName, _.Type_ID, _.Kind_ID, _.ManufacturerName_ID, _.MaxPermissibleDCVoltage,
              _.MinOperatingTemperature, _.MaxOperatingTemperature, _.MaxPermissibleDCCollectorCurrent,
              _.RadiationResistance, _.RadiationResistanceI, _.QualicationSG,
              _.QualicationЕС, _.Package, _.Remark1, _.Remark2)

    microchips = get_all(session, Microchips)
    for _ in microchips:
        print(_.ID, _.DocID, _.ComponentName, _.Type_ID, _.Kind_ID, _.ManufacturerName_ID, _.Interfaces,
              _.MinVoltage, _.MaxVoltage, _.Frequency, _.BitDepthValue, _.ConsumptionCurrent, _.TechnologyName_ID,
              _.MinOperatingTemperature, _.MaxOperatingTemperature,
              _.MemoryFormat, _.SamplingTime,
              _.RadiationResistance, _.RadiationResistanceI, _.Qualication,
              _.Package, _.Remark1)
