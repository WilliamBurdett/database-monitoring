from typing import List

from database_monitoring.exceptions import MissingVariable

DATA_TYPE_MAP = {
    0: "VARCHAR",
    1: "TIMESTAMP_NTZ",
    2: "INTEGER",
}

class Column:
    def __init__(self, column_name: str, **kwargs):
        self.column_name = column_name
        required_one_fields = ["data_type_num", "is_primary"]
        data_type_num = kwargs.get("data_type_num")
        is_primary = kwargs.get("is_primary")
        default = kwargs.get("default", "")
        not_null = kwargs.get("not_null", "")
        if data_type_num == is_primary or [data_type_num, is_primary] == [None, None]:
            raise MissingVariable(required_one_fields)
        if is_primary is not None:
            data_type_num = 2
            default = "AUTO INCREMENT"
            not_null = "NOT NULL"
        self.data_type = DATA_TYPE_MAP[data_type_num]
        self.default = default
        self.not_null = not_null
