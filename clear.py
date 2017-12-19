from random import *
import time
import os


n = 1

print(n)
time.sleep(.7)
print(3)
time.sleep(.7)
print(4)
time.sleep(.7)
os.system('cls' if os.name=='nt' else 'clear')
answer = input("enter the numbers back: ")

if answer == 134:
	print("right")
elif answer != 134: 
	print("wrong")