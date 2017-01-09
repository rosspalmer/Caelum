import math as mt

G = 6.674e-11


class Planet(object):

    def __init__(self, properties):

        self.p = properties

    def potental_energy_diff(self, mass, start_r, end_r):

        energy = G * self.p['mass'] * self.p['mass_unit'] * mass
        energy *= (1 / start_r - 1 / end_r)

        return energy

    def orbital_velocity(self, r):

        v = mt.sqrt(G * self.p['mass'] * self.p['mass_unit'] / r)
        return v
