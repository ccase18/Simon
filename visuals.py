import tkinter
class simon:
	def __init__(self):
	    IDLE = ("red", "blue", "green", "yellow")
	    FLASHED = ("#ff4d4d", "#4d4dff", "#4dff4d", "#ffff4d")

	    squares = namedtuple(Color, x, y)
	    squaresData = [square(yellow, 0, 0)
	    			   square(blue, 77, 0)
	    			   square(green,77, 77)
	    			   square(red, 0, 77)]

	    self.base = Tkinter.Tk()
	    self.Frame = Tkinter.Frame(self.base, bg="black", width= 250, height=250)

	def drawCanvas(self):

 	def flash(self):
 	
 	def reset(self):




