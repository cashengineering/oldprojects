#		python code
#		script_name: U4L22
#
#		author: Cash N.
#		description: This script allows the user to input a score between 0 & 100, after successfully entering a set of numbers the script prints the average.
#

#Libraries
from earsketch import *

#Initialization
init()
setTempo(120)

#Variable Definition
number = 0
numberOfNumbers = 0
total = 0

endDialogue = "By Entering a # Outside of the Inclusive Range [0, 100] the Loop Will Stop And Your Answer Will Be Printed."

looping = True

while looping:
  number = input("Please enter a number [0, 100] when you're done enter a number outside the range!\n" + endDialogue)
  
  try:
    number = int(number)
    
  except:
    print("Please Enter A Valid Number!")
  
  if number > 100 or number < 0:
    looping = False
    break
  
  total += number
  numberOfNumbers += 1

print("Your Average:"+str(total/numberOfNumbers))


finish()
