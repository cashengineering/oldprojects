#		python code
#		script_name: MiniTask 9
#
#		author: Cash N.
#		description: The purpose of this script is to create a song using a Nature Sample from Freesound.org
#

#Libraries
from earsketch import *

#Initializing
init()
setTempo(120)

#Sample Section
drum = EIGHT_BIT_VIDEO_GAME_LOOP_001
humming = createAudioSlice(CASHNSCHOOL_HUMMING_FIGHT, 1.1, 5)
strings = RD_CINEMATIC_SCORE_STRINGS_1

#Customized Function
def repetitive(sample1, sample2, sample3, start, end):
  fitMedia(sample1, 1, start, end)
  fitMedia(sample2, 2, start, end)

  #This Simple Loop Places the sample3 on the track 8 times 
  #starting at measure 3 when "x" is divisible by three
  for x in range (start, end):
    if x%3 == 0:
      fitMedia(sample3, 3, x, x+1)

#Function Call And Effects
repetitive(drum, humming, strings, 1, 25)

setEffect(1, VOLUME, GAIN, -20, 1)

#End
finish()
