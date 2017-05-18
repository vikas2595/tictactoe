board=list()
for row in range(3):
	board.append([])
	for col in range(3):
		board[row].append('-')
#print board
#board[2][2]='t'

for row in board:
	print "  ".join(row)

xA=input("Player A: \nvalues of x ")
yA=input("Player A: \nvalues of y ")

board[xA][yA]='X'
for row in board:
	print "  ".join(row)
import os
os.system('clear')
	
xB=input("Player B: \nvalues of x ")
yB=input("Player B: \nvalues of y ")

board[xB][yB]='O'

for row in board:
	print "  ".join(row)