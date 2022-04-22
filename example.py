import loot
import random
import pprint
from loot import string

# input the name
def wname():
  name = loot.Loot.custom_input(input("Enter Weapon's Name: "))
  print("\n")
  return name

# random name 1 to 13 characters
def rname():
  name = ''.join(random.choices(string.ascii_uppercase, k=random.randrange(1,13)))
  return name

# wpd, wpu = (1 shotgun) (2 smg) (3 ar) (4 lmg) (5 sniper) (6<= random)
# crate(amount, lowtier, hightier, wpd, wpu, [name])
def crate(amount, lowtier, hightier, wpd, wpu, name):
  objname = name
  name = dict()
  for x in range(amount):
    name[x] = loot.Loot(objname)
    name[x].roll(random.uniform(lowtier, hightier), random.randrange(wpd, wpu))
    print(objname + str(x))
    pprint.pprint(name[x].stats(), sort_dicts=False)

# crate(amount, lowtier, hightier, wpd, wpu, name)
crate(3, 0.1, 0.5, 0, 6, rname())
crate(3, 0.5, 1.5, 0, 6, rname())
