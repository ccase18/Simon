
#Game(object) API
import random

class Game 

	def__init__(self):

		self.Current_Score = s
		self.Game_Status = True 
		self.board = [ 
		[Cell("A1"), Cell("B1")],
		[Cell("A2"), Cell("B2")]		
		self.A1 = self.board[0][0] 
		self.A2 = self.board[1][0]
		self.B1 = self.board[0][1]
		self.B2 = self.board[1][1]
		]

	def input(): 
		list[]	{
		A1 = '1'
		A2 = '2'
		A3 = '3'
		A4 = '4'
		}
#Chooses a random square on the simon board and stores the value
#This stored list of squares will increase and continue as long as the user gets the order right
		r = []
		for i in range (turns):
			r = random.randint(1,4)

	def endgame():
		self.Game_Status = False 

	def scoreUp():
	    global s
	    s = s + 1
	    scoreNum.configure(text = s)

	sequence = []

	def showSequence():

	    global r
	    global sequence



def User_Input():
	A1 = Q
	A2 = W
	A3 = A 
	A4 = S
	
#The user will be able to select on certain square by clicking these keys
#Q is for the top left square. 
#W is for the top right square.
#A is for the bottom left square.
#S is for the bottom right square. 

def check_Sequence():
	global sequence

	if user_input == sequence:
		scoreUp()

	user_input = str(input('Please click the tiles our AI showed you. Click Q for the top left square. Press W for top right square. Press A for bottom left square. Press S for bottom right sqaure.'))
		
	if user_input == sequence:
		s += 5
	elif user_input != sequence:
		s == s
		endgame()

#The user will be able to select on certain square by clicking these keys
#Q is for the top left square. 
#W is for the top right square.
#A is for the bottom left square.
#S is for the bottom right square.

import time

class Time: 
	def stopwatch(self, turns):
		i = 0 
		gameState = True
		while i < turns and gameState == True:
			answer = input("You have 5 seconds, please pick a tile: ")
			self.check()
			gameState == True:
				turns = turns - 1
				self.stopwatch(turns)

	def check():
		answer = none
		time.sleep(5)
		if answer == none:
			print("too slow")
			gameState = False
		else:
			i = i 
turns = 2
mytime = Time()
mytime.stopwatch(turns)


from tkinter import *
from collections import namedtuple

class Visuals:
	def __init__(self, master):
		self.HEIGHT = 500
		self.WIDTH = 500
		self.master = master

		self.SQUARES = [(0, 249, 0, 249), (250, 500, 0, 249), (0, 249, 250, 500), (250, 500, 250, 500)]

		white = (255,255,255)
		#red = (255, 0, 0)
		#green = (0, 255, 0)
		#blue = (0, 0, 255)
		#yellow = (255, 255, 0)
		self.colors = ["red", "blue", "green", "yellow"]

		window = Tk()
		canvas = Canvas(window, width = self.WIDTH, height = self.HEIGHT, bg = "black")
		img = PhotoImage(width = self.WIDTH, height = self.HEIGHT)
		canvas.create_image((0,0), image = img, state = "normal")


	def drawRectangles(self):

		#for i in range(0, len(self.SQUARES)):
			#canvas.create_rectangle(self.SQUARES[i], fill = self.colors[i])

		canvas.pack()
		canvas.postscript(file="file_name.ps", colormode='color')


 	#def flash(self):
 		#squaretoflash = [1] #would normally be given from kevins class as a random value, but needed here
 		#for i in squarestoflash:
			#canvas.create_rectangle(SQUARES(squaretoflash), "white")
	 		#time.sleep(.6)
	 		#canvas.create_rectangle(SQUARES(squaretoflash))


 	#def reset(self):
 		#for i in range(0, len(SQUARES)):
			#canvas.create_rectangle(SQUARES(i))


root = Tk()
board = Visuals(root)
board.drawRectangles()
root.mainLoop()




