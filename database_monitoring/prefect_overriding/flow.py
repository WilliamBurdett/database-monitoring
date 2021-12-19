from prefect import Flow


class MyFlow(Flow):
    def __init__(self, name: str, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
