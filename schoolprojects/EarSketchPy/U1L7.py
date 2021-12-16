#		python code
#		script_name: MiniTask 7
#
#		author: Cash N.
#		description: The Purpose of this script is to create a custom function that
#                takes in two samples, and a starting measure to create music that lasts 48 measures on two tracks.
#

#Libraries
from earsketch import *

#Setup
init()
setTempo(220)

#Sample Section
drum = CIARA_SET_KICK_1
dubdrum = DUBSTEP_DRUMLOOP_MAIN_002

#Customized Function
def repetitive(sample1, sample2, start):
  fitMedia(sample1, 1, start, start+48)
  fitMedia(sample2, 2, start, start+48)

#Function Call
repetitive(drum, dubdrum, 1)

#End
finish()
