from system_model import System
from planet_generator import generate_planet

import math as mt
import random as rn


def generate_system(star_mass, star_lum):

    star_properties = {'mass': star_mass, 'mass_unit': 1.99e30,  # kg
                       'lum': star_lum, 'lum_unit': 3.828e26}  # W
    system = System(star_properties)

    num_planets = rn.randint(3, 12)
    dist = rn.uniform(0.100, 0.300)
    orbits = []

    for i in range(num_planets):

        orbits.append(dist)
        system.planets.append(spawn_planet(star_properties, dist))

        dist = 2 * orbits[i] * rn.uniform(0.95, 1.05)

    return system


def spawn_planet(star_properties, dist):

    prob = {'gas_giant': 3, 'ice_giant': 4, 'desert': 2,
            'ocean': 1, 'titan': 1, 'barren': 5, 'terran': 1}

    picks = []
    for planet_type in prob:
        for i in range(prob[planet_type]):
            picks.append(planet_type)

    planet_type = rn.sample(picks, 1)[0]
    planet = generate_planet(star_properties, planet_type, dist)

    return planet
