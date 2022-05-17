from  numpy import random

unit_tier = [6, 5, 4, 3]
unit_prob = [5/100, 15/100, 30/100, 50/100]

def summon(number):
    unit = random.choice(unit_tier, p=unit_prob, size=number)
    return unit

multi_summon = summon(10)

inventory = []
for x in multi_summon:
    inventory.append(x)

print(inventory)


