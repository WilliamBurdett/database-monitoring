from database_monitoring.orm.base_classes.column import Column
from inflection import tableize


class Model:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        primary_column_name = f"{tableize(class_name)}_id"
        self.primary_column = Column(primary_column_name, is_primary=True)
        self.columns = [
            self.primary_column
        ]
