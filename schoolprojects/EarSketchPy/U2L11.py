#		python code
#		script_name:
#
#		author: Cash N.
#		description: The purpose of this code is to create 16 measures of music then create a loop
#                that adds two alternating cowbell sounds for the duration of the piece.

#Libraries
from earsketch import *

#Initializing
init()
setTempo(120)

#Sample Declaration
humming = createAudioSlice(CASHNSCHOOL_HUMMING_FIGHT, 1.3, 2)
cowbell = YG_FUNK_COWBELL_1
morecowbell = YG_FUNK_COWBELL_3

#Beat Pattern Definitions
hummingBeat = "0-00+0-+0-0"
alternateBeat = "0-000+-00-+00+00"

#This For Loop Goes Through Beats One Through 24 and Adds The Normal
#'hummingBeat' if the measure isn't a mutiple of four, if it is use the alternate beat.
#The Cowbell is also alternated if the measure is a multiple of two.
for x in range (1, 16):
  makeBeat(humming, 1, x, hummingBeat if x%4 != 0 else alternateBeat)
  fitMedia(cowbell if x%2 != 0 else morecowbell, 2, x, x+1)

#End
finish()
