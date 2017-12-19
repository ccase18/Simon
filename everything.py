import random
import os
import time #these 3 are needed to make the program run
#Game(object) API

class Simon: #the Simon class
    def __init__(self,): #initializes some vars needed for the class
        self.score = 0
        self.Game_Status = True 
        self.turns = 1
        self.highscore = 0 
        self.r = [] #sequence of stored random simon square values
        

    def sequence(self):
        #Chooses a random square on the simon board and stores the value
        #This stored list of squares will increase and continue as long as the user gets the order right
        self.r.append(random.randint(1,4)) #four squares in simon, therefore 4 different numbers that can be printed
        self.printNumbers(self.r) #runs the print numbers function, printing them out


    def endgame(self): #function for when you lose
        print("Score: " + str(self.score))
        print("Highscore: " + str(self.highscore)) #prints score and highscore
        self.score = 0
        self.turns = 1 #resets the turns and score values since a game ended  
        playagain = "" #initiliazes playagain function

        while playagain != "y" and playagain != "n": #error checking
            try: 
                playagain = str(input("Would you like to play again? y/n: ")) #more error checking
            except ValueError:
                playagain = str(input("Enter y or n: "))
        #once playagain is yes or no,
        if playagain == 'y': #either restart and run the main function again
            time.sleep(.5)
            os.system('cls' if os.name=='nt' else 'clear')
            main()

        else:  #or set the game status to false, then main function
            self.Game_Status = False
            main()


    def scoreUp(self): #score up function
        self.score = self.score + (self.turns * 5) #add an increasing amount of score as the game goes on longer
        self.turns = self.turns + 1 #turn up
        if self.score > self.highscore: #if score is > than highscore, score = new highscore
            self.highscore = self.score
        else: 
            self.highscore = self.highscore #otherwise highscore stays the same
        #highscore is not reset between games, so stays constant if you keep typing y to play again
        self.sequence() #runs the sequence function once again since the user inputted the correct number(s)


    def printNumbers(self, r): #prints out the list
        for i in range(0,len(r)): #based on the length of the array
            print(self.r[i]) #print the ith number in the list out
            time.sleep(.7) #wait 0.7 seconds
            os.system('cls' if os.name=='nt' else 'clear') #wipe the terminal screen since only 1 square at a time is flashed on the simon board
            print(" ") #this is needed in case of a repeat number flashing
            time.sleep(.1) #brief blank screen then the next one
            os.system('cls' if os.name=='nt' else 'clear')
            #repeat until all numbers in the list are printed out
        os.system('cls' if os.name=='nt' else 'clear') #wipe the terminal screen to avoid the user cheating and looking
        self.check_Sequence(self.r) #run the check sequence function
  

    def check_Sequence(self, r): #function to get user input and check if it matches stored sequence of simon "square" values
        user_input = str(input('Please enter the numbers SIMON flashed to you back in the exact same order with no spaces. \n:')) #enter the numbers back
        storedvalues = ''.join(map(str, self.r)) #turns the list of simon values into a string
        if user_input == str(storedvalues): #if they are the same...
            print ("To the next level! \n \n") #next level
            time.sleep(.5) 
            os.system('cls' if os.name=='nt' else 'clear') #wait .5 seconds, then clear terminal and start again
            simon.scoreUp() #runs the scoreUp function to continue the program onward
        elif user_input != str(storedvalues): #if they are different (eg, wrong user input)
            del self.r[:] #wipe the list
            print("Wrong. Game Over.") #game over
            simon.endgame() #run the endgame function to determine if the user wants to play again


def main(): #main code
    if simon.Game_Status == True: #if gamestatus == true
        simon.sequence() #continue code
    else:
        print("Bye!") #otherwise print bye, end code


print("\nWelcome to SIMON! Just like in the real simon game, you will be flashed a seriesof numbers with each representing a different square on the simon board. Your   task it to write back this increasing list of numbers. As the game goes on, the list gets longer and the game harder. Good luck!")
time.sleep(8)
os.system('cls' if os.name=='nt' else 'clear')
simon = Simon() #initilizes the simon class
main() #runs the main loop, getting things started
    
