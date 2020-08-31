import random

verbose = True

notFinished = True
while (notFinished):
  Hat = {
    'Stephen': 'Karen',
    'Karen': 'Stephen',
    'Justin': 'Sarah',
    'Sarah': 'Justin',
    'Bryan': '',
    'Matthew': 'Jenny',
    'Jenny': 'Matthew'
  }

  Choosers = dict(Hat)

  Selections = dict()

  print ("Placing these names into the hat:")
  counter = 1
  for name,nameCannotChoose in Hat.items():
    if (counter == len(Hat)):
      prefix = "and finally, "
      suffix = "."
    else:
      prefix = ""
      suffix = ","

    if(nameCannotChoose == ""):
      print(prefix + name + suffix)
    else:
      print (prefix + name + " (who can't choose " + nameCannotChoose + ")" + suffix)
    counter += 1

  print()
  print("Now to pick the names!")

  numChoosers = len(Choosers)

  for i in range (0,numChoosers): # Randomly select who choooses a name from the hat

    if (verbose):
      print("Still to choose: ")
      for chooser in Choosers:
        print(chooser)

    chooser, chooserCannotChoose = random.choice(list(Choosers.items()))

    stillChoosing = True
    while(stillChoosing):
      drawnName, drawnNameCannotChoose = random.choice(list(Hat.items()))
      print("It is " + chooser + "'s turn..." + chooser + " reaches into the hat...and draws " + drawnName + "!")
      if (chooser == drawnName):
        if(i == numChoosers - 1):
          print("And finally, " + chooser + " will have to choose " + drawnName + " which means no Christmas for " + chooser + ". Too bad for you. :(     Just kidding! Let's just start the whole thing over...")
          stillChoosing = False
        else:
          print("But " + chooser + " clearly has to pick somebody else! Back in the hat.")
      elif(chooser == chooserCannotChoose):
        if(i == numChoosers - 1):
          print("Well that's great..." + chooser + " will have to choose " + drawnName + " which is against the rules, so " + drawnName + " won't get any presents. Bummer. :(     Just kidding! Let's just start the whole thing over...")
          stillChoosing = False
        else:
          print("But the rules say that " + chooser + " cannot choose " + chooserCannotChoose + "! Back in the hat.")
      else:
        print("This is A OK!")
        stillChoosing = False
        Selections[chooser] = drawnName
        del Hat[drawnName]
        if(i == numChoosers - 1):
          print("Congratulations! We finished an entire game and didn't break any rules!")
          notFinished = False
        
    del Choosers[chooser] # Make sure they don't choose again

print("The final results: ")
print("**************************************************************")
counter = 1
for chooser,chosen in Selections.items():
  if (counter == len(Selections)):
    prefix = "and finally, "
    suffix = "."
  else:
    prefix = ""
    suffix = ","

  print (prefix + chooser + " => is giving a gift to => " + chosen + suffix)
  counter += 1

print("**************************************************************")
# for name,constraint in Hat.items():
# print(Hat.items())
# print(len(Hat))