#		python code
#		script_name: Jukebox Project
#
#		author: Cash N.
#		description: This script creates three 16 Measure Songs, then allows the user to select one of the songs.
#                If the user does not select a song, one of the songs is chosen at random.
#

#Libraries
from earsketch import *
from random import *

#Initialization
init()

#Variables For LowTone
harp = RD_CINEMATIC_SCORE_HARP_1
drum = COMMON_LOVE_DRUMBEAT_1
chord = HOUSE_DEEP_CRYSTALCHORD_001

#Variables For HighTone
popBass = RD_POP_ARPBASS_1
drums = [HIPHOP_DUSTYGROOVE_011, HIPHOP_DUSTYGROOVE_002]
riser = RD_EDM_SFX_RISER_SQUARELEAD_1

#Variables For UnknownTone
filterChord = DUBSTEP_FILTERCHORD_002
unknownDrums = HIPHOP_DUSTYGROOVE_002

#Function Definitions
def beatSliceFill(sample, track, beat, start, end):
  """This function uses a loop to fill out a section of track using makeBeatSlice"""
  for x in range (start, end):
    makeBeatSlice(sample, track, x, beat, [1, 1.25, 1.5, 1.75])



#Song Section
def LowTone():
  #Setup And Effects
  setTempo(100)
  setEffect(1, PITCHSHIFT, PITCHSHIFT_SHIFT, -12)
  setEffect(2, VOLUME, GAIN, -60, 2, -5, 4)
  
  #Main Song Loop Used To Create A & B Sections
  for x in range (0, 9, 8):
    #A Section
    beatSliceFill(harp, 1, "3010++++12012+++", 1+x, 4+x)
    beatSliceFill(harp, 1, "3010++2+3012++++", 4+x, 5+x)
    fitMedia(drum, 2, 1.5+x, 4+x)
    
    #B Section
    fitMedia(harp, 1, 5+x, 9+x)
    fitMedia(drum, 2, 4+x, 9+x)
    beatSliceFill(chord, 3, "01+1+32101+1+321", 5+x, 8+x)
    fitMedia(chord, 3, 8+x, 9+x)
  
  

def HighTone():
  #Setup And Effects
  setTempo(120)
  setEffect(1, VOLUME, GAIN, -20, 1, 0, 3)
  setEffect(3, VOLUME, GAIN, -10)
  
  
  #Main Song Loop Used To Create A & B Sections
  for x in range (0, 9, 8):
    #A Section for Track 1
    beatSliceFill(popBass, 1, "1+2+3+++313+3+2+", 1+x, 4+x)
    beatSliceFill(popBass, 1, "1+2+3+0++2++0++1", 4+x, 5+x)
    fitMedia(drums[0], 2, 1+x, 5+x)
    
    #B Section for Track 1
    beatSliceFill(popBass, 1, "0+2+0+3++0+132+1", 5+x, 8+x)
    beatSliceFill(popBass, 1, "1+2+3+0++2++0++1", 8+x, 9+x)
    fitMedia(drums[1], 2, 5+x, 9+x)
    fitMedia(riser, 3, 1+x, 3+x)



def UnknownTone():
  #Setup And Effects And Permanent Features of The Song
  setTempo(100)
  setEffect(1, VOLUME, GAIN, -5)
  setEffect(3, VOLUME, GAIN, -5)
  
  #These Two Lines Create A Delay Without setEffect
  fitMedia(unknownDrums, 2, 1, 17)
  fitMedia(unknownDrums, 3, 1.2, 17)
  
  #Main Song Loop Used To Create A & B Sections
  for x in range (0, 9, 8):
    #A Section
    beatSliceFill(filterChord, 1, "2+3010++++12012+", 1+x, 4+x)
    beatSliceFill(filterChord, 1, "3010+31+12012++", 4+x, 5+x)
    
    #B Section
    fitMedia(filterChord, 1, 5+x, 9+x)
    
    #Temporarily Raises The Chorus On Track 1
    setEffect(1, CHORUS, CHORUS_RATE, 0.1, 7+x, 6, 7+x)
    setEffect(1, CHORUS, CHORUS_RATE, 6, 9+x, 0.1, 9+x)



#This Variable Is Here To Test With and Without The InputLoop
InputLoop = True

#Primary Input Loop Used To Select A Song And Get Information
while InputLoop:
  userInput = input("Today You'll be Selecting A Song! There are Three Songs To Choose From, LowTone, HighTone, and UnknownTone!\n "+
                    "Please Type The Name of One of The Songs To Read Its Description. Once you've made your choice, type `select {songname}:` [You can Also Type `select random` to select one at Random!] " )
  
  #This Formats the User Input So It's Easier To Compare
  userInput = userInput.lower()
  
  songNames = ["LowTone", "HighTone", "UnknownTone"]
  songChosen = ""
  endDialogue = "- Type Anything To Leave This Dialogue."
  
  #This Loop Attempts To Find The Selected Song
  for x in range (3):
    if userInput.find(songNames[x].lower()) != -1:
      songChosen = songNames[x]
  
  #If The User Is Not Selecting A Song, Display Information About The Song They've Entered
  if userInput.find("select") == -1:
    if songChosen == songNames[0]:
      input("This Is A Medium To Low Energy Song, With A Variant A and B Section. This song is more "+
            "relaxed than any other I've made thus far, yet I'm excited by how well it turned out none the less! "+ endDialogue)
    
    if songChosen == songNames[1]:
      input("This Is A High Energy Rough Around The Edges Song, With A Variant A and B Section. Though this song "+
            "has only two instruments, the song consistently delivers high energy. " + endDialogue)
    
    if songChosen == songNames[2]:
      input("It's A Mystery! " + endDialogue)
      
    else:
      print("TRACK NOT FOUND SELECT A NEW TRACK")
  
  
  
  #If The User Is Choosing A Song, Play The Song
  else:
    
    #If The User is Choosing A Song And They've Selected A Random One, Play One At Random
    if userInput.find("random") != -1:
      songChosen = songNames[randint(0, 2)]
    
    input("Playing The Song {0}. ".format(songChosen) + endDialogue)
    if songChosen.find(songNames[0]) != -1:
      LowTone()
    
    elif songChosen.find(songNames[1]) != -1:
      HighTone()
    
    elif songChosen.find(songNames[2]) != -1:
      UnknownTone()
    
    #They've Choosen A Song, Stop The Loop
    InputLoop = False



#End Script
finish()