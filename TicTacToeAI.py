import time
import os
import random
import math
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
acted = False
playergo = ["",""]
def prepicked(playergo):
	if board[playergo[0]][playergo[1]] == " ":
		return True
def wincoming():
	wins = [0,0,0,0,0,0,0,0]
	if board[0][0] == "x":
		wins[0] = wins[0]+1
		wins[3] = wins[3]+1
		wins[6] = wins[6]+1
	if board[0][1] == "x":
		wins[0] = wins[0]+1
		wins[4] = wins[4]+1
	if board[0][2] == "x":
		wins[0] = wins[0]+1
		wins[5] = wins[5]+1
		wins[7] = wins[7]+1
	if board[1][0] == "x":
		wins[1] = wins[1]+1
		wins[3] = wins[3]+1
	if board[1][1] == "x":
		wins[1] = wins[1]+1
		wins[4] = wins[4]+1
		wins[6] = wins[6]+1
		wins[7] = wins[7]+1
	if board[1][2] == "x":
		wins[1] = wins[1]+1
		wins[5] = wins[5]+1
	if board[2][0] == "x":
		wins[2] = wins[2]+1
		wins[3] = wins[3]+1
		wins[7] = wins[7]+1
	if board[2][1] == "x":
		wins[2] = wins[2]+1
		wins[4] = wins[4]+1
	if board[2][2] == "x":
		wins[2] = wins[2]+1
		wins[5] = wins[5]+1
		wins[6] = wins[6]+1
	return wins
def wincon():
	if board[0][0] == "x" and board[0][1] == "x" and board[0][2] == "x":
		return 1
	elif board[1][0] == "x" and board[1][1] == "x" and board[1][2] == "x":
		return 1
	elif board[2][0] == "x" and board[2][1] == "x" and board[2][2] == "x":
		return 1
	elif board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x":
		return 1
	elif board[0][1] == "x" and board[1][1] == "x" and board[2][1] == "x":
		return 1
	elif board[0][2] == "x" and board[1][2] == "x" and board[2][2] == "x":
		return 1
	elif board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x":
		return 1
	elif board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x":
		return 1
	elif board[0][0] == "o" and board[0][1] == "o" and board[0][2] == "o":
		return 2
	elif board[1][0] == "o" and board[1][1] == "o" and board[1][2] == "o":
		return 2
	elif board[2][0] == "o" and board[2][1] == "o" and board[2][2] == "o":
		return 2
	elif board[0][0] == "o" and board[1][0] == "o" and board[2][0] == "o":
		return 2
	elif board[0][1] == "o" and board[1][1] == "o" and board[2][1] == "o":
		return 2
	elif board[0][2] == "o" and board[1][2] == "o" and board[2][2] == "o":
		return 2
	elif board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o":
		return 2
	elif board[0][2] == "o" and board[1][1] == "o" and board[2][0] == "o":
		return 2
	elif board[0][0] != " " and board[0][1] != " " and board[0][2] != " " and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " and board[2][0] != " " and board[2][1] != " " and board[2][2] != " ":
		return 3
	else:
		return 0
playType = input("friend or AI\n")
if playType == "friend":
	while True:
		while True:
			os.system("cls")
			print("x's turn\n")
			print(board[0][2]+"0"+board[1][2]+"0"+board[2][2])
			print("00000")
			print(board[0][1]+"0"+board[1][1]+"0"+board[2][1])
			print("00000")
			print(board[0][0]+"0"+board[1][0]+"0"+board[2][0])
			playergo = input("where do you move?\n")
			playergo = eval("["+playergo+"]")
			if prepicked(playergo):
				board[playergo[0]-1][playergo[1]-1] = "x"
				break
			else:
				print("you can't do that")
			time.sleep(1)
		if wincon():
			break
		while True:
			os.system("cls")
			print("o's turn\n")
			print(board[0][2]+"0"+board[1][2]+"0"+board[2][2])
			print("00000")
			print(board[0][1]+"0"+board[1][1]+"0"+board[2][1])
			print("00000")
			print(board[0][0]+"0"+board[1][0]+"0"+board[2][0])
			playergo = input("where do you move?\n")
			playergo = eval("["+playergo+"]")
			if prepicked(playergo):
				board[playergo[0]-1][playergo[1]-1] = "o"
				break
			else:
				print("you can't do that")
			time.sleep(1)
		
		if wincon() != 0:
			break
elif playType == "AI" or playType == "ai" or playType == "Ai":
	while True:
		while True:
			os.system("cls")
			print("Your Turn")
			print(board[0][2]+"0"+board[1][2]+"0"+board[2][2])
			print("00000")
			print(board[0][1]+"0"+board[1][1]+"0"+board[2][1])
			print("00000")
			print(board[0][0]+"0"+board[1][0]+"0"+board[2][0])
			playergo = input("where do you move?\n")
			playergo = eval("["+playergo+"]")
			if prepicked([playergo[0]-1,playergo[1]-1]):
				board[playergo[0]-1][playergo[1]-1] = "x"
				break
			else:
				print("you can't do that")
			time.sleep(1)
		os.system("cls")
		if wincon():
			break
		print("")
		print(board[0][2]+"0"+board[1][2]+"0"+board[2][2])
		print("00000")
		print(board[0][1]+"0"+board[1][1]+"0"+board[2][1])
		print("00000")
		print(board[0][0]+"0"+board[1][0]+"0"+board[2][0])
		wins = wincoming()
		acted = False
		if wins[0] >= 2:
			if prepicked([0,0]):
				acted = True
				board[0][0] = "o"
			elif prepicked([0,1]):
				acted = True
				board[0][1] = "o"
			elif prepicked([0,2]):
				acted = True
				board[0][2] = "o"
		if wins[1] >= 2 and acted == False:
			if prepicked([1,0]):
				acted = True
				board[1][0] = "o"
			elif prepicked([1,1]):
				acted = True
				board[1][1] = "o"
			elif prepicked([1,2]):
				acted = True
				board[1][2] = "o"
		if wins[2] >= 2 and acted == False:
			if prepicked([2,0]):
				acted = True
				board[2][0] = "o"
			elif prepicked([2,1]):
				acted = True
				board[2][1] = "o"
			elif prepicked([2,2]):
				acted = True
				board[2][2] = "o"
		if wins[3] >= 2 and acted == False:
			if prepicked([0,0]):
				acted = True
				board[0][0] = "o"
			elif prepicked([1,0]):
				acted = True
				board[1][0] = "o"
			elif prepicked([2,0]):
				acted = True
				board[2][0] = "o"
		if wins[4] >= 2 and acted == False:
			if prepicked([0,1]):
				acted = True
				board[0][1] = "o"
			elif prepicked([1,1]):
				acted = True
				board[1][1] = "o"
			elif prepicked([2,1]):
				acted = True
				board[2][1] = "o"
		if wins[5] >= 2 and acted == False:
			if prepicked([0,2]):
				acted = True
				board[0][2] = "o"
			elif prepicked([1,2]):
				acted = True
				board[1][2] = "o"
			elif prepicked([2,2]):
				acted = True
				board[2][2] = "o"
		if wins[6] >= 2 and acted == False:
			if prepicked([0,0]):
				acted = True
				board[0][0] = "o"
			elif prepicked([1,1]):
				acted = True
				board[1][1] = "o"
			elif prepicked([2,2]):
				acted = True
				board[2][2] = "o"
		if wins[7] >= 2 and acted == False:
			if prepicked([0,2]):
				acted = True
				board[0][2] = "o"
			elif prepicked([1,1]):
				acted = True
				board[1][1] = "o"
			elif prepicked([2,0]):
				acted = True
				board[2][0] = "o"
		if acted == False:
			while True:
				guess = [math.floor(3*random.random()),math.floor(3*random.random())]
				if prepicked([guess[0],guess[1]]):
					board[guess[0]][guess[1]] = "o"
					break
		time.sleep(1)
		if wincon() != 0:
			break
if wincon() == 1:
	os.system("cls")
	print(board[0][2]+"0"+board[1][2]+"0"+board[2][2])
	print("00000")
	print(board[0][1]+"0"+board[1][1]+"0"+board[2][1])
	print("00000")
	print(board[0][0]+"0"+board[1][0]+"0"+board[2][0])
	time.sleep(2)
	os.system("cls")
	time.sleep(.5)
	print("X WINS!!!")
	print("x")
	time.sleep(1.5)
	os.system("cls")
	print("X WINS!!!")
	print("xx")
	time.sleep(1.5)
	os.system("cls")
	print("X WINS!!!")
	print("xxx")
	time.sleep(1.5)
	os.system("cls")
if wincon() == 2:
	os.system("cls")
	print(board[0][2]+"0"+board[1][2]+"0"+board[2][2])
	print("00000")
	print(board[0][1]+"0"+board[1][1]+"0"+board[2][1])
	print("00000")
	print(board[0][0]+"0"+board[1][0]+"0"+board[2][0])
	time.sleep(2)
	os.system("cls")
	time.sleep(.5)
	print("O WINS!!!")
	print("o")
	time.sleep(1.5)
	os.system("cls")
	print("O WINS!!!")
	print("oo")
	time.sleep(1.5)
	os.system("cls")
	print("O WINS!!!")
	print("ooo")
	time.sleep(1.5)
	os.system("cls")
if wincon() == 3:
	os.system("cls")
	print(board[0][2]+"0"+board[1][2]+"0"+board[2][2])
	print("00000")
	print(board[0][1]+"0"+board[1][1]+"0"+board[2][1])
	print("00000")
	print(board[0][0]+"0"+board[1][0]+"0"+board[2][0])
	time.sleep(2)
	os.system("cls")
	print("TIE")
	time.sleep(1)
	os.system("cls")
	print("TIE")
	print("WA")
	time.sleep(1)
	os.system("cls")
	print("TIE")
	print("WA - WA")
	time.sleep(1)
	os.system("cls")
	print("TIE")
	print("WA - WA - WAAAAAAAAA")
	time.sleep(2.5)