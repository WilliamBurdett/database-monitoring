from typing import List


class MissingVariable(Exception):
    def __init__(self, variable_names: List[str], *args, **kwargs):
        message = f""
        #TODO Fill in message
        super().__init__(*args, **kwargs)
