class Loot:
  def __init__(self, x):
    self.name = x
    self.acc = 0 
    self.reload = 0
    self.dmg = 0
    self.speed = 0
    self.mag = 0
    self.distance = 0
    self.recoil = 0
    self.firerate = 0

  def stats(self):
    return print(list((self.name, self.acc, self.reload, self.dmg, self.speed, self.mag, self.distance, self.recoil, self.firerate)))
  
  def roll(self, tier, type):
    # type = (1 shotgun) (2 smg) (3 ar) (4 lmg) (5 sniper)
    if type == 1:
      self.acc =  30 / tier
      self.reload = 17 / (2 * tier)
      self.dmg = pow(5, tier)
      self.speed = 750
      self.mag = 1 + tier
      self.distance = 6 + (2 * tier)
      self.recoil = 60 / tier
      self.firerate = tier / 2
    if type == 2:
      self.acc =  14 / (2 * tier)
      self.reload = 12 / (2 * tier)
      self.dmg = pow(5, tier)
      self.speed = 1200
      self.mag = 9 * tier
      self.distance = 17 + (2 * tier)
      self.recoil = 10 / tier
      self.firerate = 4 * tier
    if type == 3:
      self.acc =  8 / (2 * tier)
      self.reload = 16 / (2 * tier)
      self.dmg = 35 + pow(6, 1)
      self.speed = 1800
      self.mag = 7 * tier
      self.distance = 21 + (4 * tier)
      self.recoil = 20 / tier
      self.firerate = 2 * tier
    if type == 4:
      self.acc =  6 / (2 * tier)
      self.reload = 23 / (2 * tier)
      self.dmg = 35 + pow(6, 1)
      self.speed = 2200
      self.mag = 28 * tier
      self.distance = 42 + (4 * tier)
      self.recoil = 13 / tier
      self.firerate = 3 * tier
    if type == 5:
      self.acc = 0.5 / tier
      self.reload = 17 / (2 * tier)
      self.dmg = 70 + pow(8, tier)
      self.speed = 9999
      self.mag = 4 + tier
      self.distance = 220
      self.recoil = 70 / tier
      self.firerate = 7 / tier
