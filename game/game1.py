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
  print "################################"
  ##order the tanks and prit them out
  for myTank in sorted( tanks.keys() ):
    print myTank,tanks[myTank]

  #get the shooter
  first=raw_input("Who fires? ").lower()
  second=raw_input("Who at? ").lower()

  try:
    firstTank=tanks[first]
    secondTank=tanks[second]

  except KeyError,name:
    print "No such tank!",name
    continue

  #check if the first or the second one are alive
  if not firstTank.alive or not secondTank.alive:
    print "One of those tank is dead!"
    continue

  print
  print "*"*30
  firstTank.fire_at(secondTank)

  ##check if the victim is dead
  if not secondTank.alive:
    aliveTanks-=1

  print "*"*30

#loop through the tanks to check who was the winner
for tank in tanks.keys():
  if tanks[tank].alive :
    print tank," was the winner!"

