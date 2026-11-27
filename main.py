import sys
import random
from datetime import datetime
import csv
import argparse
import copy

parser = argparse.ArgumentParser(description='Christmas gift hat drawing')
parser.add_argument('--namelist',
                    help="""csv file with each line in the format of "name,(name-of-spouse)
                    (assumed to be in the same directory as the script)"""
                    )

args = parser.parse_args()

# Put the names in the hat:
gold_hat = {}
namelist = args.namelist
if namelist[-4:] != '.csv':
      namelist += '.csv'

with open(namelist, mode ='r')as file:
      csvFile = csv.reader(file)

      for line in csvFile:
            if len(line) == 1:
              line = [line[0], '']
            gold_hat[line[0]] = line[1]

verbose = False # Set to True for debugging information
output = "\n"

notFinished = True

output += "Welcome to the pick-name-from-the-hat game!\n"

while (notFinished):
  hat = copy.deepcopy(gold_hat)

  #Create a random list of choosers
  choosers = {k: hat[k] for k in random.sample(list(hat), len(hat))}
  Selections = dict() # Records who chose whom

  output += "\n"
  output += "Placing these names into the hat:\n"
  counter = 1
  for name,nameCannotChoose in hat.items():
    if (counter == len(hat)):
      prefix = "and finally, "
      suffix = "."
    else:
      prefix = ""
      suffix = ","

    if(nameCannotChoose == ""):
      output += prefix + name + suffix + "\n"
    else:
      output += prefix + name + " (who can't choose " + nameCannotChoose + ")" + suffix + "\n"
    counter += 1

  output += "\n"
  output += "Now to pick the names!\n"

  numChoosers = len(choosers)

  for i in range (0,numChoosers): # Randomly select who choooses a name from the hat

    if (verbose):
      output += "Still to choose: \n"
      for chooser in choosers:
        output += chooser

    # Chose who will draw a name from the hat
    chooser, chooserCannotChoose = random.choice(list(choosers.items()))
    stillChoosing = True
    while(stillChoosing):
      # Draw from the hat
      drawnName, drawnNameCannotChoose = random.choice(list(hat.items()))
      output += "It is " + chooser + "'s turn..." + chooser + " reaches into the hat...and draws " + drawnName + ". "
      # output += " *** DEBUG *** " + chooser + " cannot choose " + chooserCannotChoose + " and chose " + drawnName + "\n"
      if (chooser == drawnName):
        if(i == numChoosers - 1):
          output += "And finally, " + chooser + " will have to choose " + drawnName + " which means no Christmas for " + chooser + ". Too bad for you. :(     Just kidding! Let's just start the whole thing over...\n"
          stillChoosing = False
        else:
          output += "But " + chooser + " clearly has to pick somebody else! Back in the hat."
      elif(drawnName == chooserCannotChoose):
        if(i == numChoosers - 1):
          output += "Well that's great..." + chooser + " will have to choose " + drawnName + " which is against the rules, so " + drawnName + " won't get any presents. Bummer. :(     Just kidding! Let's just start the whole thing over...\n"
          stillChoosing = False
        else:
          output += "But the rules say that " + chooser + " cannot choose " + chooserCannotChoose + "! Back in the hat.\n"
      else:
        output += "This is A OK!\n"
        stillChoosing = False
        Selections[chooser] = drawnName
        del hat[drawnName]
        if(i == numChoosers - 1):
          output += "Congratulations! We finished an entire game and didn't break any rules!\n"
          notFinished = False
        
    del choosers[chooser] # Make sure they don't choose again

output += "The final results: \n"
output += "**************************************************************\n"
counter = 1
for chooser,chosen in Selections.items():
  if (counter == len(Selections)):
    prefix = "and finally, "
    suffix = "."
  else:
    prefix = ""
    suffix = ","

  output += prefix + chooser + " => is giving a gift to => " + chosen + suffix + "\n"
  counter += 1

output += "**************************************************************\n"

date = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
original_stdout = sys.stdout
with open("secret_santa_" + str(date) + ".txt", 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(output)
    sys.stdout = original_stdout
    
print(output)