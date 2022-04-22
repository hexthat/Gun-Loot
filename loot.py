import random
import string

class Loot:
  #if no name give random name
  def __init__(self, x=''.join(random.choices(string.ascii_uppercase, k=random.randrange(1,13)))):
    self.name = str(x)
    self.acc = 0 
    self.reload = 0
    self.dmg = 0
    self.speed = 0
    self.mag = 0
    self.distance = 0
    self.recoil = 0
    self.firerate = 0
# returns all of the Loots stats
  def stats(self):
    return {'name': [self.name], 'acc': [self.acc], 'reload': [self.reload], 'dmg': [self.dmg], 'speed': [self.speed], 'mag': [self.mag], 'distance': [self.distance], 'recoil': [self.recoil], 'firerate': [self.firerate]}
# changes Loot stats depending on tier and type
  def roll(self, tier, type):
    # type = (1 shotgun) (2 smg) (3 ar) (4 lmg) (5 sniper) (6<= random)
    # roll(tier, type)
    type = round(type)
    
    if type == 0:
      self.name = 'scrap T' + str(round(tier, 1))
      
    if type not in range(0,6):
      self.name += ' ' + str(round(tier, 1))
      self.acc = random.randrange(1, 87) / 10
      self.reload = round((random.randrange(10, 30) / (2 * tier)), 2)
      self.dmg = round((random.randrange(1,50) + pow(random.randrange(1,8), tier)))
      self.speed = round(random.choice((250, 500, 750, 1200, 1800, 2200, 9999)))
      self.mag = random.randrange(1, 75)
      self.distance = round(random.randrange(10, 1000) / 10)
      self.recoil = round(random.randrange(10,80) / tier)
      self.firerate = round(random.uniform(0.1, 7), 2)
    
    if type == 1:
      self.name += ' Shotgun T' + str(round(tier, 1))
      self.acc =  round((30 / tier), 2)
      self.reload = round((17 / (2 * tier)), 2)
      self.dmg = round((pow(5, tier)))
      self.speed = 750
      self.mag = round(1 + tier)
      self.distance = round(6 + (2 * tier))
      self.recoil = round(60 / tier)
      self.firerate =  round(tier / 2, 2)
      
    if type == 2:
      self.name += ' SMG T' + str(round(tier, 1))
      self.acc =  round((14 / (2 * tier)), 2)
      self.reload = round((12 / (2 * tier)), 2)
      self.dmg = round((pow(5, tier)))
      self.speed = 1200
      self.mag = round(9 * tier)
      self.distance = round(17 + (2 * tier))
      self.recoil = round(10 / tier)
      self.firerate =  round(4 * tier, 2)
      
    if type == 3:
      self.name += ' AR T' + str(round(tier, 1))
      self.acc =  round((8 / (2 * tier)), 2)
      self.reload = round((16 / (2 * tier)), 2)
      self.dmg = round((35 + pow(6, tier)))
      self.speed = 1800
      self.mag = round(7 * tier)
      self.distance = round(21 + (4 * tier))
      self.recoil = round(14 / tier)
      self.firerate =  round(3 * tier, 2)
      
    if type == 4:
      self.name += ' LMG T' + str(round(tier, 1))
      self.acc =  round((6 / (2 * tier)), 2)
      self.reload = round((23 / (2 * tier)), 2)
      self.dmg = round((35 + pow(6, tier)))
      self.speed = 2200
      self.mag = round(28 * tier)
      self.distance = round(42 + (4 * tier))
      self.recoil = round(20 / tier)
      self.firerate =  round(2 * tier, 2)
      
    if type == 5:
      self.name += ' Sniper T' + str(round(tier, 1))
      self.acc = round((0.5 / tier), 2)
      self.reload = round((17 / (2 * tier)), 2)
      self.dmg = round((70 + pow(8, tier)))
      self.speed = 9999
      self.mag = round(4 + tier)
      self.distance = 220
      self.recoil = round(70 / tier)
      self.firerate =  round(7 / tier, 2)
  
  # input limit by Ch3steR
  def custom_input(inp_str: str):
    try:
        assert len(inp_str) <= 15, print("More than 15 characters present")
        assert all("a" <= i <= "z" for i in inp_str), print(
            'Characters other than "a"-"z" are found'
        )
        return inp_str
    except Exception as e:
        pass
