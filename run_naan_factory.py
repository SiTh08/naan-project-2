# Functions
# def make_dough(ingredient1, ingredient2):
#     if (ingredient1 == 'wheat' or 'water') and (ingredient2 == 'water' or 'wheat'):
#         return 'dough'
#     elif (ingredient1 != 'wheat' or 'water') and (ingredient2 != 'water' or 'wheat'):
#         return 'not dough'

def make_dough(ingredient1, ingredient2):
    if (ingredient1 == 'wheat' or 'water') and (ingredient2 == 'water' or 'wheat'):
        return 'dough'
    else:
        return 'not dough'

def ru_naan_factory(ingred1, ingred2):
    # make dough
    dough_r = make_dough(ingred1, ingred2)
    #it needs to send the dough to the oven
    result_bread = wood_oven(dough_r)
    # I want it to make naan bread
    return result_bread

# def wood_oven(ingredient3):
#     if ingredient3 == 'dough':
#         return 'Naan bread'
#     elif ingredient3 != 'dough':
#         return  'Not Naan Bread'

def wood_oven(ingredient3):
    if ingredient3 == 'dough':
        return 'Naan bread'
    else:
        return 'Not Naan Bread'


# Calling of functions

print(ru_naan_factory('wheat', 'water'))


# Tests TDD
#   As a user, I can add 'wheat' and 'water' to the function make_dough, so that I can make 'dough'.
                                # evaluates --> True or False (Boolean)
print("Testing make_dough, with wheat and water --> dough to come out")
print(make_dough('wheat', 'water') == 'dough')

print("Testing make_dough, with sand and cement --> 'not dough' to come out")
print(make_dough('sand', 'cement') == 'dough')

# As a user, I can pass 'dough'  to the function oven_wood, so that I can make 'bread'.

print('Testing wood_oven, with dough --> Naan bread to come out')
print(wood_oven('dough') == 'Naan bread')

print('Testing wood_oven, with rat --> not Naan bread to come out')
print(wood_oven('rat') == 'not Naan bread')

