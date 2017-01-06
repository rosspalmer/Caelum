
class Planet(object):

    def __init__(self, properties):

        self.p = properties

    def energy_lift_mass(self, mass, start_r, end_r):

        G = 6.674e-11
        energy = G * self.p['mass'] * self.p['mass_unit'] * mass
        energy *= (1 / start_r - 1 / end_r)

        return energy
