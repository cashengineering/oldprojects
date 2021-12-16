#		python code
#		script_name: U3L18
#
#		author: Cash N.
#		description: This script loops through four drum sounds and plays them in order over 16 measures.
#

from earsketch import *

init()
setTempo(120)

drums = [CIARA_SET_PERC_CLAP_1, CIARA_SET_PERC_DISTBASS, CIARA_SET_PERC_HIHAT_2, CIARA_SET_PERC_HIHAT_3]

for x in range (0, len(drums)):
  #This math makes sure that each of the samples gets played for four full measures
  fitMedia(drums[x], 1, (x*4)+1, ((x+1)*4)+1)

finish()
