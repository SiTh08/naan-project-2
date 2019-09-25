def make_dough(ingredient1, ingredient2):
    if (ingredient1 == 'wheat' or 'water') and (ingredient2 == 'water' or 'wheat'):
        return 'dough'
    else:
        return 'not dough'

def wood_oven(ingredient3):
    if ingredient3 == 'dough':
        return 'Naan bread'
    else:
        return 'not Naan bread'

def ru_naan_factory(ingred1, ingred2):
    # make dough
    dough_r = make_dough(ingred1, ingred2)
    #it needs to send the dough to the oven
    result_bread = wood_oven(dough_r)
    # I want it to make naan bread
    return result_bread