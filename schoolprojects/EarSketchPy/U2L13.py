#		python code
#		script_name: Repetition Lab
#
#		author: Cash N.
#		description: This script creates an 8 measure song that introduces a drum using
#                makebeat which then swaps beat's order during the second half of the song. 
#

#Libraries
from earsketch import *

#Initialization 
init()
setTempo(120)

#Variable Section
drum = EIGHT_BIT_VIDEO_GAME_LOOP_003
drum2 = HIPHOP_HIHAT_ROLL_001
drum3 = HIPHOP_STOMP_BEAT_001
lead = MILKNSIZZ_ADIOS_LATIN_808
beat = "0++0+0+-0+0+++"

#Function Section
def beatSwapper(sample, start, end, beat):
  """
  This function takes in a sample, start measure, end measure, and a beat
  then will place them on the DAW Using makeBeat. Additionally,
  this function will swap the beat's first and second half for the
  latter half of the song.
  """
  
  #The beatHalf ternary is superfluous given that stringSlicing doesn't care
  #if the number being entered was not cleanly divisble by two.
  
  beatHalf = len(beat)/2 if len(beat)%2 == 0 else (len(beat)-1)/2
  #Beat Start slices the beat from the start to the middle of the beat
  beatStart = beat[0:beatHalf]
  #Beat End slices the beat from the middle to the end of the beat
  beatEnd = beat[beatHalf::]

  #Use beat for the sample ? If x is not half way through the given range : Else use beatEnd+beatStart
  for x in range (start, end):
    makeBeat(sample, 1, x, beat if x<=end/2 else beatEnd + beatStart)

#Set Effect and Function Call
beatSwapper(drum3, 1, 9, beat)
setEffect(1, VOLUME, GAIN, -5)

#End
finish()