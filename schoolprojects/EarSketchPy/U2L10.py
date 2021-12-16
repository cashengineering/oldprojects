#		python code
#		script_name: MiniTask10
#
#		author: Cash N.
#		description: This script creates a custom beat from the previously used Humming Bird sample.
#

#Libraries
from earsketch import *

#Initializing
init()
setTempo(120)

#Sample Section
drum = EIGHT_BIT_VIDEO_GAME_LOOP_001
humming = createAudioSlice(CASHNSCHOOL_HUMMING_FIGHT, 1.3, 2)
piano = Y05_PIANO_2

hummingBeat = "0-00+0-+0-0"
alternateBeat = "0-000+-00-+00+00"

#This For Loop Goes Through Beats One Through 24 and Adds The Normal
#'hummingBeat' if the measure isn't a mutiple of four, if it is use the alternate beat.
for x in range (1, 24):
  makeBeat(humming, 1, x, hummingBeat if x%4 != 0 else alternateBeat)

#This Section Adds The Effects and the non-beat Samples to the Track
fitMedia(drum, 2, 1, 24)
fitMedia(piano, 3, 6, 24)
setEffect(1, DISTORTION, DISTO_GAIN, 5, 1)
setEffect(2, VOLUME, GAIN, -20, 1)
setEffect(3, VOLUME, GAIN, -10, 1)

#End
finish()
