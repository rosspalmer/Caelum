
def display_system(system):

    print('========================')
    print(' - Star Mass: %f' % system.star['mass'])
    print(' - Star Lum: %f' % system.star['lum'])

    i = 1

    for planet in system.planets:

        print('')
        print('>> Planet %i' % i)
        print('')
        print(' - Type: %s' % planet.p['planet_type'])
        print(' - Mass: %f' % planet.p['mass'])
        print(' - Radius: %f' % planet.p['radius'])
        print(' - Dist: %f AU' % planet.p['au'])
        print('')
        print(' - Period: %f Days' % planet.p['period'])
        print(' - Rotation: %f Days' % planet.p['rotation'])
        print('')
        print(' - Temp: %f K' % planet.p['temp'])
        if 'atm' in planet.p:
            print(' - Atmosphere: %f atm' % planet.p['atm'])
        print(' - Alb: %f' % planet.p['alb'])
        print('')
        print(' - Radius: %f' % planet.p['radius'])
        print(' - Density: %f' % planet.p['density'])
        print(' - Gravity: %f g' % planet.p['g'])

        i += 1
