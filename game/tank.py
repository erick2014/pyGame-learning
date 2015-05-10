#class that im going to import
class Tank(object):

  def __init__(self, name):
    self.name = name
    self.alive = True
    self.ammo = 5
    self.armor = 60
    self.result=""

  def __str__(self):
    if self.alive:
      return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
    else:
      return "%s (DEAD)" % self.name

  def fire_at(self, enemy):
    if self.ammo >= 1:
      self.ammo -= 1
      print self.name, "fires on", enemy.name
      self.result=enemy.hit()

    else:
      self.result=self.name, "has no shells!"
      print result

    return self.result

  def hit(self):

    self.armor -= 20
    self.result=self.name+" is hit!"
    print self.result
    print "%s's remaining life is %i" % (self.name,self.armor)

    if self.armor <= 0:
      self.result=self.explode()

    return self.result

  def explode(self):
    self.alive = False
    print self.name, "explodes!"
    return "isDead"
