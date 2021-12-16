#		python code
#		script_name: U4L23
#
#		author: Cash N.
#		description: This script asks the user to choose between three types of music then will create
#                music based upon the choosen dictionary.
#

#Libaries
from earsketch import *

#Initialization
init()
setTempo(120)

#Variable Definitions

cinema = {
  1: RD_CINEMATIC_SCORE_MAINDRUM_2,
  4: RD_CINEMATIC_SCORE_DRUMPART_3,
  7: RD_CINEMATIC_SCORE_HARP_2,
  10: RD_CINEMATIC_SCORE_HARP_4,
}

funk = {
  1: YG_FUNK_CONGO_1,
  4: YG_FUNK_ELECTRIC_PIANO_1,
  7: YG_FUNK_FUNK_GUITAR_1,
  10: YG_FUNK_HIHAT_1
}

pop = {
  1: YG_NEW_FUNK_GUITAR_1,
  4: YG_ALT_POP_CHORDS_1,
  7: YG_ALT_POP_HIHAT_1,
  10: YG_ALT_POP_OPENHAT_1
}

selectedDictionary = {}


"""
This Loop Allows the user to select a genre then simply plays four samples from the genre.
"""
while True:
  userInput = input("Please Choose A Song Genre By Entering A Number: Cinema [1], Funk [2], Pop [3].")

  print(userInput)
  selectedDictionary.clear()
  
  if userInput == "1":
    for key, item in cinema.items():
      fitMedia(item, 1, key, key+3)
    break
  
  if userInput == "2":
    for key, item in funk.items():
      fitMedia(item, 1, key, key+3)
    break
    
  if userInput == "3":
    for key, item in pop.items():
      fitMedia(item, 1, key, key+3)
    break

for key, item in selectedDictionary:
  fitMedia(item, 1, key, key+3)

#End
finish()