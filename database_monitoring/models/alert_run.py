from database_monitoring.orm.Model import Model


class AlertRun(Model):
    def __init__(self, *args, **kwargs):
        super().__init__()
