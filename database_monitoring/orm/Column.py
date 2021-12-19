from database_monitoring.orm.DataType import DataType


class Column:
    def __init__(self, column_name: str, data_type: DataType):
        self.column_name = column_name
        self.data_type = data_type
