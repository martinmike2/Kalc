class Orbit:
    pe = None
    ap = None
    sma = None

    def __init__(self, connection):
        self.pe = connection.space_center.active_vessel.orbit.periapsis
        self.ap = connection.space_center.active_vessel.orbit.apoapsis
        self.sma = (self.pe + self.ap) / 2
        
    def __init__(self, pe: int, ap: int) -> object:
        self.pe = pe
        self.ap = ap
        self.sma = (pe + ap) / 2