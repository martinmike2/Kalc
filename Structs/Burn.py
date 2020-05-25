class Burn:
    prograde :int = None
    normal :int = None
    radial :int = None
    time :int = None

    def __init__(self, prograde: int):
        self.prograde = prograde
        self.normal = 0
        self.radial = 0
        self.time = 0