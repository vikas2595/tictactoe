import os
import sys
from termcolor import colored,cprint


def inputA():

	iA=input("\nPlayer A: value of i ")

	jA=input("Player A: value of j ")

	if(iA<0 or iA>2 or jA<0 or jA>2):

		cprint("Invalid values....Enter again",'red')

		inputA()

	return iA,jA



def inputB():	

	iB=input("\nPlayer B: value of i ")

	jB=input("Player B: value of j ")

	if(iB<0)or(iB>2)or(jB<0)or(jB>2):

		cprint("Invalid values....Enter again",'red')

		inputB()

	return iB,jB

def welcome():
	cprint("\t\t+************************+",'yellow')
	cprint("\t\t| Welcome to Tic Tac Toe |",'cyan')
	cprint("\t\t+************************+",'yellow')


def aldydrA():

	xA,yA=inputA()

	if(matrix[xA][yA]=='X' or matrix[xA][yA]=='O'):

			cprint("\nAlready occupied...place your X somewhere else\n",'red')

			aldydrA()

	os.system('clear')

	welcome()

	return xA,yA



def aldydrB():

	xB,yB=inputB()

	if(matrix[xB][yB]=='X' or matrix[xB][yB]=='O'):

			cprint("\nAlready occupied...place your O somewhere else\n",'red')

			aldydrB()

	os.system('clear')

	welcome()

	return xB,yB



def showBoard():

	print "\n"

	i=0

	for row in matrix:

		print "\t","   	 ".join(row),"\t\t",i,"0","  ",i,"1","  ",i,"2","\n\n"

		i=i+1



def win(board):

		if (board[0][0]==board[0][1]==board[0][2]=='X') or (board[1][0]==board[1][1]==board[1][2]=='X') or (board[2][0]==board[2][1]==board[2][2]=='X') or (board[0][0]==board[1][0]==board[2][0]=='X') or (board[0][1]==board[1][1]==board[2][1]=='X') or (board[0][2]==board[1][2]==board[2][2]=='X') or (board[1][1]==board[2][2]==board[0][0]=='X') or (board[0][2]==board[1][1]==board[2][0]=='X'):

			cprint("\nPlayer 1 has won\n",'yellow')

			return 'A'

		if (board[0][0]==board[0][1]==board[0][2]=='O') or (board[1][0]==board[1][1]==board[1][2]=='O') or (board[2][0]==board[2][1]==board[2][2]=='O') or (board[0][0]==board[1][0]==board[2][0]=='O') or (board[0][1]==board[1][1]==board[2][1]=='O') or (board[0][2]==board[1][2]==board[2][2]=='O') or (board[1][1]==board[2][2]==board[0][0]=='O') or (board[0][2]==board[1][1]==board[2][0]=='O'):

			cprint("\nPlayer 2 has won\n",'yellow')

			return 'B'

			
matrix=list()

for row in range(3):

	matrix.append([])

	for col in range(3):

		matrix[row].append('--')



os.system('clear')

welcome()

showBoard()



for i in range(0,10):

	if i%2==0:

		xA,yA=aldydrA()

		matrix[xA][yA]='X'

		os.system('clear')

		welcome()

		showBoard()

	else:

		xB,yB=aldydrB()

		matrix[xB][yB]='O'

		os.system('clear')

		welcome()

		showBoard()

	win(matrix)

	if win(matrix)=='A':
		cprint("\n Congratulations",'cyan')
	if win(matrix)=='B':
		cprint("\n Congratulations",'cyan')
	else:
		cprint("\nGame Draw",'red')