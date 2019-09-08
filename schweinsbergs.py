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
LeftEar.color('orange')



LeftEar.penup()
LeftEar.setpos(0,150)
LeftEar.pendown()
LeftEar.left(90)
LeftEar.begin_fill()
for lear in range(2):
    LeftEar.forward(100)
    LeftEar.right(160)
LeftEar.end_fill()

LeftEar.left(180)
LeftEar.forward(50)
LeftEar.penup()

#######################################################################################################################
#Draw eyes
#######################################################################################################################

BadEye = turtle.Turtle()
BadEye.color('black')
BadEye.shape('circle')
BadEye.penup()
BadEye.setpos(20,70)
BadEye.pendown()

BadEye.hideturtle()

BadEye.left(50)
BadEye.forward(40)
BadEye.penup()
BadEye.setpos(40,70)
BadEye.pendown()
BadEye.left(90)
BadEye.forward(40)

Goodeye = turtle.Turtle()
Goodeye.color('yellow')
Goodeye.shape('circle')
Goodeye.hideturtle()
Goodeye.penup()
Goodeye.setpos(130,70)
Goodeye.pendown()
Goodeye.begin_fill()
for ge in range(4):
    Goodeye.left(90)
    Goodeye.forward(32)
Goodeye.end_fill()

#######################################################################################################################
#Draw Nose
#######################################################################################################################

nose = turtle.Turtle()
nose.color('pink')
nose.shape('arrow')
nose.penup()
nose.setpos(73,48)
nose.right(90)





wn.exitonclick()          # keeps the dang window open



