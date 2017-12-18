import time

class Time: 
	def stopwatch(self, turns):
		i = 0 
		gameState = True
		while i < turns and gameState == True:
			answer = input("You have 5 seconds, please pick a tile: ")
			self.check()
			while gameState == True:
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