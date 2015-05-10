#class that im going to import
class Tank(object):

  def __init__(self, name):
    self.name = name
    self.alive = True
    self.ammo = 5
    self.armor = 60
    self.deadMan=""

  def __str__(self):
    if self.alive:
      return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
    else:
      return "%s (DEAD)" % self.name

  def fire_at(self, enemy):
    result=""
    print "################################"
    if self.ammo >= 1:
      self.ammo -= 1
      print self.name, "fires on", enemy.name
      result=enemy.hit()

    else:
      result="noAmmo"
      print self.name, "has no shells!"

    return result

  def hit(self):
    result=""

    self.armor -= 20
    print self.name+" is hit!"
    print "%s's remaining life is %i" % (self.name,self.armor)
    result="hit"

    if self.armor <= 0:
      self.explode()
      result="dead"

    return result

  def explode(self):
    self.alive = False
    print "xxxxxxxxxxxxxxxxxxxxx"
    print self.name, "explodes!"
    print "xxxxxxxxxxxxxxxxxxxxx"
