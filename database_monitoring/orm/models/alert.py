from database_monitoring.orm.base_classes.model import Model


class Alert(Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
