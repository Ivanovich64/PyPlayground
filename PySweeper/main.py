    #  #  #  #  #  #  #
   #  #  #  #  #  #  #
  #  # PySweeper #  #
 #  #  #  #  #  #  #
#  #  #  #  #  #  #

# by: PieChai
# Python 3.8.2
# Enjoy

from matrixFunc import *
from validations import *




# Welcome Screen
print(" Welcome to PySweeper ".center(35,"~")+"\n Select your difficulty:\n (1) Crybaby\n (2) n00b\n (3) Yeah, I lift bro.\n (4) I've installed Gentoo one-handed and only half screen working.\n (5) Whatever.\n (10000) Surprise Me. \n (0) wtf is this, I wanna get out!")
#map=makeMtrx(validateDiff(input("\n\n> ")))
showMap(makeMtrx(takeDiff(validateDiff(input("\n\n > ")))))
#print(map)
