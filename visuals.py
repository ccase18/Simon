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


