from universe_model import Universe
from system_generator import generate_system

import math as mt
import pandas as pd


def generate_universe():

    stars = pd.read_csv('star_data.csv')
    stars['id'] = stars.index

    systems = []

    for star in stars.to_dict('records'):

        mass = estimate_star_mass(star['lum'])
        system = generate_system(mass, star['lum'])

        systems.append(system)

    return Universe(systems)


def estimate_star_mass(lum):

    M_sun = 1.99e30  # kg

    mass = mt.pow(lum * mt.pow(M_sun, 2.3) / 0.23, (1 / 2.3))
    mass = mass / M_sun

    if mass < 0.43:
        return mass

    mass = mt.pow(lum, 0.25) * M_sun
    mass = mass / M_sun

    if mass < 2:
        return mass

    mass = mt.pow(lum * mt.pow(M_sun, 3.5) / 1.5, (1 / 3.5))
    mass = mass / M_sun

    if mass < 20:
        return mass

    mass = lum * M_sun / 3200
    mass = mass / M_sun

    return mass

generate_universe()
