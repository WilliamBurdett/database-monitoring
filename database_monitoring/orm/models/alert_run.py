from database_monitoring.orm.base_classes.model import Model


class AlertRun(Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns.append(
            
        )
