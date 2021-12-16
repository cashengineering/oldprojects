#		python code
#		script_name: MiniTask 3 
#
#		author: Cash N.
#		description: This code creates eight measures of music that utilize the
#                setEffect command to add a delay and reduce the volume.
#

#Libraries
from earsketch import *

#Variables Set To Constants
keys = RD_POP_KEYPLUCK_1
horns = Y17_HORNS_1
drums = CIARA_SET_DRUMBEAT_1

#Setup
init()
setTempo(120)

#Music
fitMedia(keys, 1, 1, 9)
fitMedia(horns, 2, 5, 9)
fitMedia(drums, 3, 3, 9)

#Effects used to create a Delay and Volume Decrease
setEffect(1, DELAY, MIX, 0.2)
setEffect(2, VOLUME, GAIN, -5)

#End Program
finish()