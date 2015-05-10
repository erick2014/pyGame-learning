from tank import Tank

##create some tanks with its own name
tanks = {
          "alice":Tank("Alice"),
          "bob":Tank("Bob"),
          "carol":Tank("Carol")
        }

aliveTanks=len(tanks)

while aliveTanks > 1:

  #validate the victims
  try :
    #get the shooter
    first=raw_input("Who fires? ").lower()
    first=tanks[first]
    #get the victim
    second=raw_input("Who at? ").lower()
    second=tanks[second]

  except KeyError,name:
    print "No such tank!",name
    continue

  #shoot
  result=first.fire_at(second)
  print "result",result


