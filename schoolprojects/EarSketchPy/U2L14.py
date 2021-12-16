#		python code
#		script_name: MiniTask14/Lab15
#
#		author: Cash N.
#		description: The purpose of this script is to debug the provided script, and make it work without any runtime errors.
#

# python code
# script_name: U2L14
# author: Earsketch Team
# description: This 20-second song uses custom functions, delay effects, and makeBeat.

from earsketch import *
#Setup
init()
setTempo(120)

#Create a drum beat for the transition
fillSnare = "0+++0+++0+0+0000"
drumBeatA = "0+++0+++0+0+0000"
drumInstrument = OS_CLAP01

#Music
# A section
#This function's second argument, endMeasure, was misspelled.
def sectionA(startMeasure, endMeasure):
  #This line has been commented out to stop redefining a variable that the function specifically calls for.
  #endMeasure = startMeasure + 4
  for measure in range(startMeasure, endMeasure):
    fitMedia(DUBSTEP_LEAD_013, 1, measure, measure + 1)
    fitMedia(RD_FUTURE_DUBSTEP_PAD_2, 2, measure, measure + 1)
    #Insert our original drum beat string
    makeBeat(drumInstrument, 4, measure, drumBeatA)

# B section
def sectionB(startMeasure, endMeasure):
  #This line has been commented out to stop redefining a variable that the function specifically calls for.
  #endMeasure = startMeasure + 6
  for measure in range(startMeasure, endMeasure):
    fitMedia(DUBSTEP_LEAD_015, 1, measure, measure + 1)
    fitMedia(RD_FUTURE_DUBSTEP_PAD_2, 2, measure, measure + 1)
    #Modify our original drum beat string to swap the first and second halves
    drumBeatB = drumBeatA[10: 27] + drumBeatA[1: 10]
    makeBeat(drumInstrument, 4, measure, drumBeatB)

#Call our functions to create sections
sectionA(1, 5)
sectionB(5, 10)
sectionA(10, 15)
sectionB(15, 20)

#This line has been changed so that it extends from 20, instead of 19
insertMediaSection(drumInstrument, 4, 20, 1, 5)   #Extends drumbeat to the end
makeBeat(OS_SNARE02, 3, 8.5, fillSnare)
makeBeat(OS_SNARE02, 3, 13.5, fillSnare)
makeBeat(OS_SNARE02, 3, 18.5, fillSnare)

#Add an effect to the snare fill
setEffect(3, DELAY, DELAY_TIME, 1200.0)

#Finish
finish()