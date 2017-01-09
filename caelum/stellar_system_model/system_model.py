import math as mt

G = 6.674e-11


class System(object):

    def __init__(self, star_properties):

        self.star = star_properties
        self.planets = []
        self.ships = {}

    def transfer_energy(self, mass, start_planet, end_planet):

        r_start = self.planets[start_planet - 1].p['semi_axis']
        r_end = self.planets[end_planet - 1].p['semi_axis']
        r_total = r_start + r_end

        u = G * self.star['mass'] * self.star['mass_unit']
        v_1 = mt.sqrt(u / r_start) * (mt.sqrt(2 * r_end / r_total) - 1)
        v_2 = mt.sqrt(u / r_end) * (1 - mt.sqrt(2 * r_start / r_total))

        energy = (1 / 2) * mass * (v_1 + v_2)

        return energy

    def move_ship(self, ship_name, planet_num):

        ship = self.ship[ship_name]

        energy_required = self.transfer_energy(ship.p['mass'],
                                               ship.planet, planet_num)

        if ship.energy >= energy_required:

            ship.energy -= energy_required
            ship.planet = planet_num

        self.ships[ship_name] = ship
