import loot
import pprint

# str name of loot
gun1 = loot.Loot('Test')

# tier = weapon stat multiplier
# type = (0 scrap) (1 shotgun) (2 smg) (3 ar) (4 lmg) (5 sniper) (6<= random)
# roll(tier, type)
gun1.roll(1,4)

gun2 = loot.Loot('Test2')
gun2.roll(1,6)
# print the stats of loot
pprint.pprint(gun1.stats(), sort_dicts=False)
pprint.pprint(gun2.stats(), sort_dicts=False)
