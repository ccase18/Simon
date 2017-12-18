#Game(object) API
class Game 

	def__init__(self, object):

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
	
	def User_Input():
		[0][1] = Q
		[1][1] = W
		[1][0] = A 
		[1][1] = S
#The user will be able to select on certain square by clicking these keys
#Q is for the top left square. 
#W is for the top right square.
#A is for the bottom left square.
#S is for the bottom right square. 
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

	def showSequence():

	    global r
	    global sequence

	    if r == 1:

	    elif r == 2:

	    elif r == 3:  

	    elif r == 4:



		
