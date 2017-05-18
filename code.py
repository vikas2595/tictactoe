import os

def inputA():
	iA=input("\nPlayer A: value of i ")
	jA=input("Player A: value of j ")
	if(iA<0 or iA>2 or jA<0 or jA>2):
		print "Invalid values....Enter again"
		inputA()
	return iA,jA

def inputB():	
	iB=input("\nPlayer B: value of i ")
	jB=input("Player B: value of j ")
	if(iB<0)or(iB>2)or(jB<0)or(jB>2):
		print "Invalid values....Enter again"
		inputB()
	return iB,jB

def aldydrA():
	xA,yA=inputA()
	if(board[xA][yA]=='X' or board[xA][yA]=='O'):
			print "\nAlready occupied...place your X somewhere else\n"
			aldydrA()
	os.system('clear')
	print "\t\t+************************+"
	print "\t\t| Welcome to Tic Tac Toe |"
	print "\t\t+************************+"
	return xA,yA

def aldydrB():
	xB,yB=inputB()
	if(board[xB][yB]=='X' or board[xB][yB]=='O'):
			print "\nAlready occupied...place your O somewhere else\n"
			aldydrB()
	os.system('clear')
	print "\t\t+************************+"
	print "\t\t| Welcome to Tic Tac Toe |"
	print "\t\t+************************+"
	return xB,yB

def showBoard():
	print "\n"
	i=0
	for row in board:
		print "\t","   	 ".join(row),"\t\t",i,"0","  ",i,"1","  ",i,"2","\n\n"
		i=i+1

def win(board):
		if (board[0][0]==board[0][1]==board[0][2]=='X') or (board[1][0]==board[1][1]==board[1][2]=='X') or (board[2][0]==board[2][1]==board[2][2]=='X') or (board[0][0]==board[1][0]==board[2][0]=='X') or (board[0][1]==board[1][1]==board[2][1]=='X') or (board[0][2]==board[1][2]==board[2][2]=='X') or (board[1][1]==board[2][2]==board[0][0]=='X') or (board[0][2]==board[1][1]==board[2][0]=='X'):
			print "\nPlayer 1 has won\n"
			return 'A'
		if (board[0][0]==board[0][1]==board[0][2]=='O') or (board[1][0]==board[1][1]==board[1][2]=='O') or (board[2][0]==board[2][1]==board[2][2]=='O') or (board[0][0]==board[1][0]==board[2][0]=='O') or (board[0][1]==board[1][1]==board[2][1]=='O') or (board[0][2]==board[1][2]==board[2][2]=='O') or (board[1][1]==board[2][2]==board[0][0]=='O') or (board[0][2]==board[1][1]==board[2][0]=='O'):
			print "\nPlayer 2 has won\n"
			return 'B'
			



board=list()
for row in range(3):
	board.append([])
	for col in range(3):
		board[row].append('--')

os.system('clear')
print "\t\t+************************+"
print "\t\t| Welcome to Tic Tac Toe |"
print "\t\t+************************+"
showBoard()

for i in range(0,10):
	if i%2==0:
		xA,yA=aldydrA()
		board[xA][yA]='X'
		os.system('clear')
		print "\t\t+************************+"
		print "\t\t| Welcome to Tic Tac Toe |"
		print "\t\t+************************+"
		showBoard()
	else:
		xB,yB=aldydrB()
		board[xB][yB]='O'
		os.system('clear')
		print "\t\t+************************+"
		print "\t\t| Welcome to Tic Tac Toe |"
		print "\t\t+************************+"
		showBoard()
	win(board)
	if win(board)=='A' or win(board)=='B':
		break