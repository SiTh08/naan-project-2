from naan_functions import *

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