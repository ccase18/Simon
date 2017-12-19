import random
import os
import time
#Game(object) API

class Simon:

	def __init__(self,):
		self.score = 0
		self.Game_Status = True 
		self.turns = 1
		self.highscore = 0
		self.r = []
		
	def sequence(self): 
#Chooses a random square on the simon board and stores the value
#This stored list of squares will increase and continue as long as the user gets the order right
		self.r.append(random.randint(1,4))
		self.printNumbers(self.r)


	def endgame(self):
		print("Score: " + str(self.score))
		print("Highscore: " + str(self.highscore))
		self.score = 0
		self.turns = 1
		try: 
			playagain = str(input("Would you like to play again? y/n: "))
		except ValueError:
			playagain = str(input("Enter y or n: "))

		if playagain == 'y':
			main()
		else: 
			self.Game_Status = False



		self.Game_Status = False 


	def scoreUp(self):
	    self.score = self.score + (self.turns * 5)
	    self.turns = self.turns + 1
	    if self.score > self.highscore:
	    	self.highscore = self.score
	    else: 
	    	self.highscore = self.highscore
		self.sequence()

	def printNumbers(self, r):
		for i in range(0,len(r)):
			print(self.r[i])
			time.sleep(.7)
		os.system('cls' if os.name=='nt' else 'clear')
		check_Sequence(self.r)


"""class Time: 
	def stopwatch(self, turns):
		i = 0 
		gameState = True
		while i < turns and gameState == True:
			answer = input("You have 5 seconds, please pick a tile: ")
			self.check()
			gameState == True:
				turns = turns - 1
				self.stopwatch(turns)

	def check(self):
		answer = none
		time.sleep(5)
		if answer == none:
			print("too slow")
			gameState = False
		else:
			i = i """


def check_Sequence(r):
	user_input = str(input('Please enter the numbers SIMON flashed to you back in the exact same order with no spaces. \n: '))
	storedvalues = ''.join(map(str, simon.r))
	if user_input == str(storedvalues):
		print ("To the next level! \n \n")
		time.sleep(.5)
		os.system('cls' if os.name=='nt' else 'clear')
		simon.scoreUp()
	elif user_input != str(storedvalues):
		del r[:]
		print("Wrong. Game Over.")
		simon.Game_Status = False
		simon.endgame()


def main():
	if simon.Game_Status == True:
		simon.sequence()
	else:
		print("Bye!")

simon = Simon()
main()
	
