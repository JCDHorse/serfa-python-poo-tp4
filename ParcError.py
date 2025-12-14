
# Création d'exception pour une gestion d'erreurs plus simple
# Bonus non demandé par le TP

class ParcError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"{msg}")

class StationError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"{msg}")
