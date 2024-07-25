from sqlalchemy.orm import sessionmaker

from db_proc.db_oim_orm import (Manufacturers, ComponentTypes, ComponentKinds, Technologies, Diods,
                                Resistors, Transistors, Microchips, Capacitors, db_tables)
from db_proc.db_get_data import get_all
from db_proc.db_connect import get_connection_mssql


class ComponentDB:
    table_list = [Microchips, Resistors, Diods, Capacitors, Transistors, Manufacturers, Technologies,
                  ComponentKinds, ComponentTypes]
    table_list_names = db_tables
    data = []
    current_table_index = None

    def __init__(self):
        engine = get_connection_mssql()
        session_obj = sessionmaker(bind=engine)
        self.session = session_obj()

    def queue_table_data(self, table_index):
        self.current_table_index = table_index
        self.data.clear()
        self.data.extend(get_all(self.session, self.table_list[table_index]))

    def get_table_data(self):
        return self.data

    @property
    def row_count(self):
        return len(self.data)

    @property
    def column_count(self):
        column_num = 0
        if len(self.data) > 0:
            column_num = self.data[0].column_num
        return column_num

    @property
    def column_names(self):
        names = []
        if len(self.data) > 0:
            return self.data[0].column_names
        return tuple(names)

