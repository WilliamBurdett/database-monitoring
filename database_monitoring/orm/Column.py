from database_monitoring.orm.DataType import DataType


class Column:
    def __init__(
        self,
        column_name: str,
        data_type_num: int = None,
        primary_key: bool = False,
        default_now: bool = False,
    ):
        self.data_type = DataType(data_type_num)
        self.column_name = column_name
        self.primary_key = primary_key
        self.default_now = default_now
