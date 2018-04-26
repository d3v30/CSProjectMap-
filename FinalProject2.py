# import libraries 
from turtle import *
from time import sleep
import sys
import time
 
#create dictionaries
leo = {
'turtle': Turtle(),
'color': "blue",
'speed': 15,
'image': "leo.gif",
}

mikey = {
'turtle': Turtle(),
'color': "orange",
'speed': 10,
'image': "mikey.gif",
}


#globalizing the values of direction 
global up
global down
global left
global right
up = False
down = False
left = False
right = False

#set images for characters for user interface 
leoscreen = leo['turtle'].getscreen()
leoscreen.addshape(leo['image'])
leo['turtle'].shape(leo['image'])
leo['turtle'].penup()
leo['turtle'].shape('turtle')
leo['turtle'].color(leo['color'])

mikeyscreen = mikey['turtle'].getscreen()
mikeyscreen.addshape(mikey['image'])
mikey['turtle'].shape(mikey['image'])
mikey['turtle'].penup()
mikey['turtle'].shape('turtle')
mikey['turtle'].color(mikey['color'])

#defining functions for moving leo in the game 
def ld():
	global up
	global down
	global left
	global right
	# globalize the value of the direction leo moves 
	left = False
	up = False
	down = False
	if right == False: 
		leo['turtle'].setheading(0)
		right = True
	leo['turtle'].fd(leo['speed'])
	print(leo['turtle'].pos())
	check()
	print(str(up) + str(down) + str(left) + str(right))

	def la():
	global up
	global down
	global left
	global right
	# globalize the value of the direction the turtle moves 
	right = False
	up = False
	down = False
	if left == False: 
		leo['turtle'].setheading(180)
		left = True
	leo['turtle'].fd(leo['speed'])
	print(leo['turtle'].pos())
	print(str(up) + str(down) + str(left) + str(right))
	check()
def lw():
	global up
	global down
	global left
	global right
	# globalize the value of the direction the turtle moves 
	left = False
	right = False
	down = False
	if up == False: 
		leo['turtle'].setheading(90)
		up = True
	leo['turtle'].fd(leo['speed'])
	print(leo['turtle'].pos())
	check()
	print(str(up) + str(down) + str(left) + str(right))
def ls():
	global up
	global down
	global left
	global right
	# globalize the value of the direction the turtle moves 
	left = False
	up = False
	right = False
	if down == False: 
		leo['turtle'].setheading(270)
		down = True
	leo['turtle'].fd(leo['speed'])
	print(leo['turtle'].pos())
	check()
	print(str(up) + str(down) + str(left) + str(right))
#defining mikey
def md():
	leoscreen.listen()
	global up
	global down
	global left
	global right
	# globalize the value of the direction the turtle moves 
	left = False
	up = False
	down = False
	if right == False: 
		mikey['turtle'].setheading(0)
		right = True
	mikey['turtle'].fd(mikey['speed'])
	print(mikey['turtle'].pos())
	check()
	# function checks for position after every time it moves the turtle 
def ma():
	global up
	global down
	global left
	global right
	# globalize the value of the direction the turtle moves 
	right = False
	up = False
	down = False
	if left == False: 
		mikey['turtle'].setheading(180)
		left = True
	mikey['turtle'].fd(mikey['speed'])
	print(mikey['turtle'].pos())
	check()
def mw():
	global up
	global down
	global left
	global right
	# globalize the value of the direction the turtle moves 
	left = False
	right = False
	down = False
	if up == False: 
		mikey['turtle'].setheading(90)
		up = True
	mikey['turtle'].fd(mikey['speed'])
	print(mikey['turtle'].pos())
	check()
def ms():
	global up
	global down
	global left
	global right
	left = False
	up = False
	right = False
	# globalize the value of the direction the turtle moves 
	if down == False: 
		mikey['turtle'].setheading(270)
		down = True
	mikey['turtle'].fd(mikey['speed'])
	print(mikey['turtle'].pos())
	check()
def dd():
	leoscreen.listen()
	global up
	global down
	global left
	global right
	# globalize the value of the direction the turtle moves 
	left = False
	up = False
	down = False
	if right == False: 
		don['turtle'].setheading(0)
		right = True
	don['turtle'].fd(don['speed'])
	print(don['turtle'].pos())
	check()
def da():
	global up
	global down
	global left
	global right
	# globalize the value of the direction the turtle moves 
	right = False
	up = False
	down = False
	if left == False: 
		don['turtle'].setheading(180)
		left = True
	don['turtle'].fd(don['speed'])
	print(don['turtle'].pos())
	check()
def check():
	if leo['turtle'].xcor() > 300 or leo['turtle'].xcor() < -300 or leo['turtle'].ycor() < -300 or leo['turtle'].ycor() > 300:
		#we need to make sure that the characters are in the field of view 
		global hitpoints
		print("Out of x or bounds!!!")

# leo's movements based off location and key strokes 
# key strokes must match the direction 
leoscreen.onkeypress(ld, "d")
leoscreen.onkeypress(la, "a")
leoscreen.onkeypress(lw, "w")
leoscreen.onkeypress(ls, "s")
# mikey's movements based off location and key strokes 
# key strokes must match the direction 
mikeyscreen.onkeypress(md, "Right")
mikeyscreen.onkeypress(ma, "Left")
mikeyscreen.onkeypress(mw, "Up")
mikeyscreen.onkeypress(ms, "Down")


#currently in the process of trying to alter/find a new map 
#this is the zelda map
#We're trying to alter it and change the setting complelety 
#but still will be 2d with similiar layout.
#https://www.pygame.org/project-NES+Zelda+Map+Data-2741-.html
import pygame, sys, os, pprint, time, pyganim
from pygame.locals import *


#All weeek we additionally did research on python crash course and stack overflow about manipulating the map
#Specifically, we were trying to learn how to make the buildings solid, so the characters can not walk through them
#We also worked on getting GitHub, however we are currently have trouble finishing the last steps

