#		python code
#		script_name: MiniTask 5
#
#		author: Cash N.
#		description: This code creates sixteen measures of music that utilize the reverb and distortion effects.
#

#Libraries
from earsketch import *

#Variables Set To Constants
harp = RD_CINEMATIC_SCORE_HARP_3
pad = EIGHT_BIT_ATARI_PAD_001
moog = HIPHOP_DUSTYMOOG_001
drum = HIPHOP_STOMP_BEAT_PART_005

#Setup
init()
setTempo(120)

#Music
fitMedia(harp, 1, 1, 17)
fitMedia(pad, 2, 4, 17)

#This Simple Loop Places the "moog" sample on the track 7 times 
#    starting at measure 3 when "x" isn't divisible by two
for x in range (0, 14):
  if x%2 != 0:
    fitMedia(moog, 3, x+3, x+4)

#Effects used to create a Reverb on Track One and Distortion on Track Two, with lowered volumes
#    on track two, and three.
setEffect(1, REVERB, MIX, 0.5)
setEffect(2, DISTORTION, DISTO_GAIN, 5)
setEffect(2, VOLUME, GAIN, -10, 1)
setEffect(3, VOLUME, GAIN, -5, 1)

#End Program
finish()