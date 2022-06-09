from  numpy import random

unit_tier = [6, 5, 5, 4, 4, 4]
unit_prob = [1/100, 7/100, 9/100, 25/100, 28/100, 30/100]

def summon(number):
    unit = random.choice(unit_tier, p=unit_prob, size=number)
    return unit

multi_summon = summon(10)

inventory = []
for x in multi_summon:
    inventory.append(x)

print(inventory)


