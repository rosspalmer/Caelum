
def display_system(system):

    print('========================')
    print(' - Star Mass: %.2f' % system.star['mass'])
    print(' - Star Lum: %.2f' % system.star['lum'])

    i = 1

    for planet in system.planets:

        print('')
        print('>> Planet %i' % i)
        print('')

        display_planet(planet)

        i += 1


def display_planet(planet):

    print(' - Type: %s' % planet.p['planet_type'])
    print(' - Mass: %.2f' % planet.p['mass'])
    print(' - Dist: %.2f AU' % planet.p['au'])
    print('')
    print(' - Period: %.2f Days' % planet.p['period'])
    print(' - Rotation: %.2f Days' % planet.p['rotation'])
    print('')
    print(' - Temp: %.2f K' % planet.p['temp'])
    if 'atm' in planet.p:
        print(' - Atmosphere: %.2f atm' % planet.p['atm'])
    print(' - Alb: %.2f' % planet.p['alb'])
    print('')
    print(' - Radius: %.2f' % planet.p['radius'])
    print(' - Density: %.2f' % planet.p['density'])
    print(' - Gravity: %.2f g' % planet.p['g'])
