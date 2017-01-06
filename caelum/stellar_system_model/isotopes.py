
def isotope_ratios(element):

    ratios = {'H': {'H2': {'water': 1.56e-4, 'comet': 3e-4,
                           'ice_giant': 4e-5, 'gas_giant': 1e-5}}}

    isotopes = ratios[element]

    return isotopes
