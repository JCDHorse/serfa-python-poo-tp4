
class ParcError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"{msg}")

class StationError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"{msg}")
