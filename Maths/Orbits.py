import numpy as np

from Structs.Burn import Burn
from Structs.Orbit import Orbit


class OrbitMaths:

    def __init__(self, connection):
        self.connection = connection
        self.mu = self.connection.space_center.active_vessel.orbit.body.gravitational_parameter

    def vis_viva(self, r, a):
        return np.sqrt(self.mu * (2 / r - 1 / a))

    def hohmann(self, parking: Orbit, target: Orbit):
        v_park = self.vis_viva(parking.sma, parking.sma)
        t_sma = (parking.sma + target.sma) / 2
        t_vp = self.vis_viva(parking.pe, t_sma)

        injection = Burn(prograde=(t_vp - v_park))

        t_va = self.vis_viva(target.ap, t_sma)
        v_target = self.vis_viva(target.sma, target.sma)

        circ = Burn(prograde=(v_target - t_va))

        return [injection, circ]
