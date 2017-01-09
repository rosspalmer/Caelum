

def adjust_for_isotopes(element_ratio, source):

    ir = isotope_ratios()

    output = dict(element_ratio)

    for element in element_ratio:

        if element in ir:

            initial_ratio = element_ratio[element]
            base_ratio = 1

            for isotope in ir[element]:

                output[isotope] = initial_ratio * ir[element][isotope][source]
                base_ratio -= ir[element][isotope][source]

            output[element] *= base_ratio

    return output


def isotope_ratios():

    ratios = {'H': {'H2': {'water': 1.56e-4, 'comet': 3e-4,
                           'ice_giant': 4e-5, 'gas_giant': 1e-5}}}

    return ratios
