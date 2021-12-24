from database_monitoring.orm.base_classes.model import Model


class Alert(Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns.append(Column("inserted_timestamp", data_type="TIMESTAMP_NTZ", default="CURRENT_TIMESTAMP"))
