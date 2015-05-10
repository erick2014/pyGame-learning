class Tank(object):
    #define the constructor
    def __init__(self,name,alive):
        self.name =name
        self.alive=alive
        self.ammo=5
        self.armor=6

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name,self.armor,self.ammo)
        else:
            return "%s (DEAD)"% self.name
#test list

#create an instance of Tank
myTank=Tank("Bob",False)
##test
print myTank
props=vars(myTank)
#iterate through class properties
'''
'for p in props:
    print "property: "+p+" value: "+str(props[p])
    #print props[p]
'''





