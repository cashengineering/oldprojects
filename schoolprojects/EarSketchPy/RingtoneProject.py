#		python code
#		script_name: Ringtone Challenge
#
#		author: Cash N.
#		description: This script creates a 60 second ringtone for a watch company
#                requiring high efficiency code and excellent music.
#

#Library Imports
from earsketch import *

#Initialization + Tempo
init()
setTempo(100)

#Variable Definitions
beatA = "0+1+2++3++33+11+"
beatBList = ["0++++1+2++1+2++", "0++++1+01+0+1+-", "00000000"]
strings = RD_WORLD_PERCUSSION_ETHNICSTRING_2
drums = EIGHT_BIT_VIDEO_GAME_LOOP_017


#Function Definitions
def beatSliceFill(sample, track, beat, start, end):
  """This function uses a loop to fill out a section of track using makeBeatSlice"""
  for x in range (start, end):
    makeBeatSlice(sample, track, x, beat, [1, 1.25, 1.5, 1.75])

def modifiedBeatSlice(samples, track, beats, start, end):
  """
  This function combines two of the beatSliceFill functions to create a varation in track
  by replacing the first instrument with the second on the last beat of the the given start and end times.
  Notably this function can's parameters take in either a string or list for both "samples" and "beats".
  This function can handle tracks and beats being the same length, or having tracks/beats have a length
  of one while the latter remaining variable is a list longer than the former.
  """
  
  #This logic determines if the beatsBeforeSwap should be based upon the number of beats or samples
  beatsBeforeSwap = end-len(beats)+1 if type(beats) is not str else end
  if beatsBeforeSwap > end-len(samples)+1 and type(samples) is not str:
    beatsBeforeSwap = end-len(samples)+1
  
  #This line fills in the first sample until before the swap is made
  beatSliceFill(samples if type(samples) is not list else samples[0], track, beats if type(beats) is str else beats[0], 
                start, beatsBeforeSwap)

  #This statement deals with only one sample but many beats
  if type(samples) is not list and beatsBeforeSwap != end:
    for y in range (0, len(beats)-1):
      #This uses beatSliceFill to fill in one measure at a time, based upon the current beat #
      beatSliceFill(samples, track, beats[y+1], beatsBeforeSwap+y, beatsBeforeSwap+y+1)
    return

  #This for loop deals with many samples but only one beat
  for x in range (1, len(samples)):
    beatsBeforeSwap = end-len(samples)
    #This uses beatSliceFill to fill in one measure at a time, based upon the current sample #
    beatSliceFill(samples[x], track, beats if type(beats) is str else beats[x], 
                  beatsBeforeSwap+x, beatsBeforeSwap+x+1)



#This function mostly acts as a tool to help the song be looped, as it will ensure that
def songLoop(start, end):
  """
  This function mostly acts as a tool to help the song be looped, as the "song" is
  eight measures long and is repeated three times. The logic within this function allows
  it to repeat it's main theme every four measures with eight measures having an extra drum section.
  """
  for x in range (start, (end/4)+1):
    #This math ensures that a section only repeats every four measures
    newStart = (x if x == 1 else ((x-1)*4)+1)
    newEnd = (x*4)+1
    #These function calls create the primary theme of the piece
    modifiedBeatSlice([strings, strings], 1, [beatA, beatA[0:9]+"2++2+1+"], newStart, newEnd)
    modifiedBeatSlice(drums, 2, beatBList, newStart, newEnd)
    
    #This places an extra drum sample every eight measures.
    if (newEnd-1)%8 is 0:
      beatSliceFill(drums, 3, "----1212+2+", newEnd-2, newEnd)



"""Function Calls and Effects"""
songLoop(1, 25)
#This changes the notes in track A to sound 12 notes lower in pitch
setEffect(1, PITCHSHIFT, PITCHSHIFT_SHIFT, -12)
#For loop that creates a fade in for tracks 1-3 with track 3 having a lower final-gain
for x in range (1, 4):
  setEffect(x, VOLUME, GAIN, -40, 1, -5 if x != 3 else -10, 4)

#This effect removes the higher harsher frequencies from tracks 2 & 3
setEffect(2, FILTER, FILTER_FREQ, 1500)
setEffect(3, FILTER, FILTER_FREQ, 1500)


#End Script
finish()