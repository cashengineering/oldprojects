#		python code
#		script_name: U3L20
#
#		author: Cash N.
#		description: This script uses makeBeat to play a sample once with a beat then
#                remix that beat three more times until a random 48 Beat-Long String is Derived


#Library Import
from earsketch import *
from random import *

#Initialization
init()
setTempo(120)

#Variable Definitions
drums = [EIGHT_BIT_ANALOG_DRUM_LOOP_001, EIGHT_BIT_ANALOG_DRUM_LOOP_006, DUBSTEP_PERCDRUM_002]
drumChoice = drums[randint(0, 2)]
print(drumChoice)
beat = "0++-0+0+--0+0000"
newBeat = ""

#Function Definitions

#This function gets a psuedo-random beat type with a 5/8 bias towards it's input
def getBiasedBeat(original):
    random = randint(1, 8)
    
    if random == 1:
      return("0")
    
    if random == 2:
      return("+")

    if(random) == 3:
      return("-")
    
    else:
      return(original)

#Music Section
makeBeat(drumChoice, 1, 1, beat)

#This Loops Through 3 Times To Create 48 Full Sixteenth Notes
for y in range (0, 3):
  #This Adds a new beat every time to be remixed again
  newBeat += beat

  #This will loop through somewhere between 4 & 8 Times in order to not remix the whole string 
  for x in range (randint(4, 8)):
    #This Picks A Random # Somwhere In The Range Of The Most Recent [16th Note] Section
    randomValue = randint(1+(y*16), 15+(y*16))
    
    #This replaces a character by add everything up to it minus one,
    #then randomizing it, and then adding everything after it
    newBeat = newBeat[:randomValue-1] + getBiasedBeat(newBeat[randomValue]) + newBeat[randomValue:]

#Creates The New Remixed 3x Version of the beat
makeBeat(drumChoice, 1, 2, newBeat)

#End
finish()