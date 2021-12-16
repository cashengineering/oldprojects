#		python code
#		script_name: Challenge Unit 1
#
#		author: Cash N.
#		description: The purpose of this code is to write a working and short
#                    piece of music in order to reflect the values of the
#                    Boys and Girls Club of Ada County.

#Libraries
from earsketch import *

#Variables Set To Constants
chordsSound = YG_ALT_POP_PIANO_1
leadSound = RD_UK_HOUSE__WARMPIANO_1
drumSound = YG_ALT_POP_SNARE_4

#Setup
init()
setTempo(90)

#Music
fitMedia(chordsSound, 1, 1, 8)
fitMedia(leadSound, 2, 1, 8)
fitMedia(drumSound, 3, 1, 8)

#Effects used to create a gentle and calm fade-in
setEffect(1, VOLUME, GAIN, -20, 1, -5, 4)
setEffect(3, VOLUME, GAIN, -30, 1, -10, 4)

#Effects used to create a relaxing fade-out
setEffect(1, VOLUME, GAIN, -5, 7, -50, 8)
setEffect(2, VOLUME, GAIN, 0, 7, -50, 8)
setEffect(3, VOLUME, GAIN, -10, 7, -50, 8)

#End Program
finish()