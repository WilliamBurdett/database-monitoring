from typing import List

from database_monitoring.orm import DataType
from database_monitoring.orm.Column import Column


class Model:
    def __init__(self):
        self.columns = [
            Column("id", data_type_num=DataType.INT, primary_key=True),
            Column("inserted_timestamp", data_type_num=DataType.TIMESTAMP, default_now=True),
        ]
