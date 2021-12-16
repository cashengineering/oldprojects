#		python code
#		script_name: MiniTask 3 
#
#		author: Cash N.
#		description: This code creates eight measures of music that utilize the
#                setEffect command to add a delay and create a fade in and fade out.
#

#Libraries
from earsketch import *

#Variables Set To Constants
keys = Y02_KEYS_1
voice = YG_HOUSE_VOX_2
drums = CIARA_SET_DRUMBEAT_1

#Setup
init()
setTempo(120)

#Music
fitMedia(keys, 1, 1, 17)
fitMedia(voice, 2, 5, 13)
fitMedia(drums, 3, 3, 17)

#Effects used to create a Delay, Fade In and Fade Out
setEffect(1, DELAY, MIX, 0.2)
setEffect(1, VOLUME, GAIN, -20, 1, -5, 4)
setEffect(1, VOLUME, GAIN, -5, 7, -60, 17)
setEffect(3, VOLUME, GAIN, -20, 5)

#End Program
finish()