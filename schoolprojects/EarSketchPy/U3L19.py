#		python code
#		script_name: U3L19
#
#		author: Cash N.
#		description: This code loops through 4 Drum Samples in A List over 8 Measures then does the same in reverse.
#

#Library Import
from earsketch import *

#Initialization
init()
setTempo(120)

#Variable Definitions
drums = [CIARA_SET_PERC_CLAP_1, CIARA_SET_PERC_DISTBASS, CIARA_SET_PERC_HIHAT_2, CIARA_SET_PERC_HIHAT_3]

#Music Section
for x in range (0, len(drums)):
  #This math makes sure that each of the samples gets played for two full measures
  fitMedia(drums[x], 1, (x*2)+1, ((x+1)*2)+1)

#This Line Reverses the "drums" array
drums = drums[::-1]

for x in range (len(drums), len(drums)*2):
  #The change between this for loop and the previous one is the ranges
  #this causes the sample call to have to subtract 4, but other than that the math is identical
  fitMedia(drums[x-4], 1, (x*2)+1, ((x+1)*2)+1)

#End
finish()