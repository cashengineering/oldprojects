#		python code
#		script_name: MiniTask 8
#
#		author: Cash N.
#		description: This script for the purpose of practicing collaboration and working together.
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














