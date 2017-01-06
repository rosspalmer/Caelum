from planet_model import Planet

import math as mt
import random as rn

M_jupiter = 2e27  # kg
R_jupiter = 71492  # km
M_earth = 6e24  # kg
R_earth = 6378  # km


def generate_planet(star_properties, planet_type, au):

    parameters = {'gas_giant': {'atmosphere': {'H': 0.9, 'He': 0.1},
                                'mass_unit': M_jupiter,
                                'min_mass': 0.5, 'max_mass': 8,
                                'radius_unit': R_jupiter,
                                'min_r': 0.8, 'max_r': 1.5,
                                'min_a': 0.2, 'max_a': 0.4},

                  'ice_giant': {'atmosphere': {'H': 0.8, 'He': 0.2},
                                'mass_unit': M_jupiter,
                                'min_mass': 0.3, 'max_mass': 1.5,
                                'radius_unit': R_jupiter,
                                'min_r': 0.3, 'max_r': 0.8,
                                'min_a': 0.2, 'max_a': 0.4},

                  'desert': {'atmosphere': {},
                             'atm_min': 0.01, 'atm_max': 0.5,
                             'mass_unit': M_earth,
                             'min_mass': 0.5, 'max_mass': 3,
                             'radius_unit': R_earth,
                             'min_a': 0.1, 'max_a': 0.6},

                  'ocean': {'atmosphere': {},
                            'atm_min': 0.5, 'atm_max': 10,
                            'mass_unit': M_earth,
                            'min_mass': 0.5, 'max_mass': 3,
                            'radius_unit': R_earth,
                            'min_a': 0.03, 'max_a': 0.1},

                  'titan': {'atmosphere': {},
                            'atm_min': 0.5, 'atm_max': 10,
                            'mass_unit': M_earth,
                            'min_mass': 0.5, 'max_mass': 3,
                            'radius_unit': R_earth,
                            'min_a': 0.5, 'max_a': 0.8},

                  'terran': {'atmosphere': {},
                             'atm_min': 0.5, 'atm_max': 10,
                             'mass_unit': M_earth,
                             'min_mass': 0.5, 'max_mass': 3,
                             'radius_unit': R_earth,
                             'min_a': 0.3, 'max_a': 0.6},

                  'barren': {'mass_unit': M_earth,
                             'min_mass': 0.5, 'max_mass': 3,
                             'radius_unit': R_earth,
                             'min_a': 0.1, 'max_a': 0.3}

                  }

    param = parameters[planet_type]

    prop = {'planet_type': planet_type, 'au': au}

    prop['mass'] = rn.uniform(round(param['min_mass'], 4),
                              round(param['max_mass'], 4))
    prop['mass_unit'] = param['mass_unit']

    if 'min_r' not in param and 'max_r' not in param:
        prop['radius'] = rn.normalvariate(prop['mass'], 0.1)
    else:
        prop['radius'] = rn.uniform(round(param['min_r'], 4),
                                    round(param['max_r'], 4))
    prop['radius_unit'] = param['radius_unit']

    volume = (4 / 3) * mt.pi * mt.pow(prop['radius'], 3)
    prop['density'] = prop['mass'] / volume
    prop['g'] = calc_gravity(prop)

    prop['semi_axis'] = prop['au'] * 1.496e11  # meters
    period_sec = calc_period(prop, star_properties)  # seconds
    prop['period'] = period_sec / (24 * 60 * 60)

    prop['rot'] = rn.random()
    prop['rotation'] = calc_rotation(prop)  # days

    if 'atm_min' in param:
        prop['atm'] = rn.uniform(round(param['atm_min'], 4),
                                 round(param['atm_max'], 4))
    prop['alb'] = rn.uniform(round(param['min_a'], 4),
                             round(param['max_a'], 4))
    prop['temp'] = calc_temp(prop, star_properties)  # K

    return Planet(prop)


def calc_period(prop, star):

    G = 6.674e-11
    u = G * star['mass'] * star['mass_unit']

    period = 2 * mt.pi * mt.sqrt((mt.pow(prop['semi_axis'], 3) / u))

    return period


def calc_temp(prop, star):

    A_ratio = (prop['rot'] * 0.25) + 0.25
    prop_constant = 5.67e-8

    num = A_ratio * star['lum'] * star['lum_unit'] * (1 - prop['alb'])
    #|Note 0.96 is emission which should be modeled later
    dem = 4 * mt.pi * prop_constant * 0.96 * mt.pow(prop['semi_axis'], 2)

    temp = mt.pow(num / dem, 0.25)

    return temp


def calc_rotation(prop):

    rotation = prop['rot'] * (30 - 1) + 1  # days

    return rotation


def calc_gravity(prop):

    earth_ratio = 5.98e24 / mt.pow(1.276e7, 2)
    planet_ratio = (prop['mass'] * prop['mass_unit']) / \
                    mt.pow(prop['radius'] * prop['radius_unit'] * 1000, 2)

    gravity = planet_ratio / earth_ratio

    return gravity