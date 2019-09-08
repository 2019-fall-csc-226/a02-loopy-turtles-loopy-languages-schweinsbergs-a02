######################################################################
# Author: Samantha Schweinsberg
# Username: schweinsbergs
#
# Assignment: A02: Loopy Turtles
# Purpose: To draw something I enjoy
######################################################################
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle              # importing turtles

wn = turtle.Screen()       # making screen



kittyhead = turtle.Turtle()     # creating and configuring the head attributes
kittyhead.shape('arrow')
kittyhead.color('orange')

head = 5
pen = 10

######################################################################################################################
# Draw the head
######################################################################################################################

kittyhead.begin_fill()
for khead in range(6):
    kittyhead.forward(150)
    kittyhead.left(90)
kittyhead.end_fill()

kittyhead.right(90)

#######################################################################################################################
# Draw right ear
#######################################################################################################################
kittyhead.begin_fill()
for khead in range(2):
    kittyhead.forward(100)
    kittyhead.left(160)
kittyhead.end_fill()

kittyhead.left(180)
kittyhead.forward(30)
kittyhead.penup()

#######################################################################################################################
# draw left ear
######################################################################################################################
LeftEar = turtle.Turtle()
LeftEar.shape('arrow')
LeftEar.color('black')










wn.exitonclick()          # keeps the dang window open



