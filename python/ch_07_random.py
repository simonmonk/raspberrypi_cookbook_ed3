import random
from copy import copy

list = ['a', 'b', 'c']

working_list = copy(list)
while len(working_list) > 0 :
    x = random.choice(working_list)
    print(x)
    working_list.remove(x)
