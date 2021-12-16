#		python code
#		script_name: U3L17
#
#		author: Cash N.
#		description: Gives the user two choices of effects, and will add them conditionally.
#

#Libraries
from earsketch import *

#Initialization
init()
setTempo(120)

#Variable Definitions
kalimba = RD_WORLD_PERCUSSION_KALIMBA_PIANO_2
funkdot = HIPHOP_FUNKDOT_001
intro = HOUSE_SFX_WHOOSH_001
questions = ["Do you want the Kalimba? [Y/N]", "Do you want the Funkdot? [Y/N]",
             "Do you want a Delay on Track 1 (This is the track the Kailmba would play on)? [Y/}"]

#This function looks through the string to see if a "Y" was entered, and return a boolean based upon that answer
def responseEvaluate(response):
  if response.lower().find("y") != -1:
    return True
    
  else:
    return False

#This loop runs through the questions and performs logic based upon responses
for x in range (len(questions)):
  booleanAnswer = responseEvaluate(readInput(questions[x]))
  #If the responseEvaluator is True then based upon the question # perform logic to add things
  if booleanAnswer:
    if x == 0:
      fitMedia(kalimba, x+1, 3, 9)
      
    if x == 1:
      fitMedia(funkdot, x+1, 3, 9)
      
    if x == 2:
      setEffect(1, DELAY, DELAY_TIME, 1200.0)

fitMedia(intro, len(questions)+1, 1, 3)  

#End
finish()