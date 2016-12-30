
M_jupiter = 1.898e27
M_earth = 5.972e24


class Planet(object):

    def __init__(self):
        pass


def random_pick():

    prob = {'gas_giant': 1, 'ice_giant': 1, 'desert': 1,
            'ocean': 1, 'titan': 1, 'barren': 1, 'terran': 1}

    picks = []
    for planet_type in prob:
        for i in range(prob[planet_type]):
            picks.append(planet_type)

    return prob


def gas_giant():

    prop = dict()

    prop['min_mass'] = 0.5*M_jupiter
    prop['max_mass'] = 4*M_jupiter

    prop['atmosphere'] = {'H': 0.9, 'He': 0.1}

    return prop


def ice_giant():

    prop = dict()

    prop['min_mass'] = 0.1*M_jupiter
    prop['max_mass'] = 0.5*M_jupiter

    prop['atmosphere'] = {'H': 0.8, 'He': 0.2}

    return prop


def desert():

    prop = dict()

    prop['min_mass'] = 0.5*M_earth
    prop['max_mass'] = 3*M_earth

    prop['atm_min'] = 0.0001
    prop['atm_max'] = 1

    return prop


