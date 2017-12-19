
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

