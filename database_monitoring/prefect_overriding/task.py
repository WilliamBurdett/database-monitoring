from prefect import Task


class MyTask(Task):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
