#		python code
#		script_name: U4L24
#
#		author: Cash N.
#		description: This script asks the user to choose between two vocal samples, then a class
#                will create eight measures of the selected vocal sample.
#

#Libraries
from earsketch import *

#Initialization
init()
setTempo(140)

#Variable Definitions
vocals = [Y20_SHOUT_1, Y33_CHOIR_1]



#Class Definitions
class musicMaker():
  
  def __init__(self, samples):
    self.userInput = None
    self.samples = samples
  
  
  
  def getChoice(self):
    if self.userInput == None:
      
      while True:
        self.userInput = input("Choose Your Vocal Sample! Shout [1] or Choir [2]!")
        try:
          
          self.userInput = int(self.userInput)
          
          if self.userInput == 1:
            print("You have choosen sample 1")
            break
            
          if self.userInput == 2:
            print("You have choosen sample 2")
            break
            
          else:
            print("You have choosen an invalid sample!")
        
        except:
          print("Please Enter A Valid Number!")



  def playMusic(self):
    fitMedia(self.samples[self.userInput-1], 1, 1, 9)




#Main Music Section
maker = musicMaker(vocals)
maker.getChoice()
maker.playMusic()

#End
finish()