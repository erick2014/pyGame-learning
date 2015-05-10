from tank import Tank

##create some tanks with its own name
tanks = {
          "alice":Tank("Alice"),
          "bob":Tank("Bob"),
          "carol":Tank("Carol")
        }

aliveTanks=len(tanks)
secondName=""
result=""

while aliveTanks > 1:

  #validate the victims
  try :
    print "################################"
    #get the shooter
    first=raw_input("Who fires? ").lower()
    first=tanks[first]

    #get the victim
    second=raw_input("Who at? ").lower()
    secondName=second
    second=tanks[second]

  except KeyError,name:
    print "The enemy doesnt exists or is dead",name
    continue

  #shoot
  result=first.fire_at(second)

  if ( result == "dead" ):
    aliveTanks-=1
    #remove the victim who dies
    del tanks[secondName]

print "Who wins the fight?",tanks.keys()
print "Congratz nigga!"


