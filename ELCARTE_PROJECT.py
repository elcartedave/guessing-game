import time
import random
import os
high_score={}

def Menu(x): #x here is 'gold'
	print()
	print("========Memorization Game========\n")
	time.sleep(0.5)
	print("Welcome to the CMSC TYPE-THE-PATTERN GAME!\n")
	print("Gold:", x)
	time.sleep(0.5)
	print("[1] Start Game")
	print("[2] View Scores")
	print("[3] Delete Scores")
	print("[4] Shop")
	print("[5] Instructions")
	print("[6] Exit\n")
	choice=int(input("Please enter a number: "))
	return choice

def score(x,y,z,q):
	points1=x*y*z*q
	if q!=1:
		print("Multiplier:",q)
	return points1

def patterncreator(x,y,z): #(c,alpha,z)
	length=0
	pattern=""
	while length<x:
			number=random.randint(0,z)
			length=length+1
			pattern=pattern + y[number]
	return pattern

def game(x,y,z,w,v,q): #(c,alpha,z,gold,plus_lives,multiplier)
	lives=3+v
	point=0
	streak=1 #number of streak answered correctly
	correct_pattern="" #shows the last pattern answered correctly
	long_streak=0 #shows the longest streak by the player
	while True:
		pattern=patterncreator(x,y,z)
		print("The pattern is:\n")
		print(pattern)
		print()
		time.sleep(0.3)
		print("Memorize it in...")
		print("5")
		time.sleep(1)
		print("4")
		time.sleep(1)
		print("3")
		time.sleep(1)
		print("2")
		time.sleep(1)
		print("1")
		time.sleep(1)
		os.system('clear')
		guess=input("Please enter the pattern: ")
		i=0
		while i<len(pattern):
			if len(pattern)!=len(guess):
				indicator=1
				break
			elif guess[i]==pattern[i]:
				indicator=0
			elif guess[i]!=pattern[i]:
				indicator=1
				break
			i=i+1
		if indicator==1:
			time.sleep(0.3)
			streak=1
			if lives>0:
				print("=============================\n")
				print("The code is incorrect, please try again\n")
				lives=lives-1
				print("Lives:", lives)
				print("The correct pattern is", pattern)
				print("Your current score is", point)
				print()
				print("=============================\n")
				n=input("PRESS ANY KEY TO CONTINUE: ")
				os.system('clear')
			else:
				print("░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░")
				print("██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗")
				print("██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝")
				print("██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗")
				print("╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║")
				print("░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")
				print("The correct pattern is", pattern)
				print("Lives ran out! Please try again!")
				print("Final Score:",point)
				print("Current gold:", w)
				if correct_pattern=="":
					return_values=[point,"No correct pattern",long_streak, w] #w is gold
				else:
					return_values=[point,correct_pattern,long_streak, w] #w is gold
				return return_values
				break
		else:
			correct_pattern=pattern
			time.sleep(0.3)
			print("=============================\n")
			print("WOW! The code is correct!\n")
			print("Lives:", lives)
			score1=score(x,z,streak,q) #(c,z,streak,multiplier)
			print(point,"+ (",x*z,"x", streak,"(Streak))")
			point=score1+point
			print("Your current score is", point)
			if streak>=1:
				print("Your current streak is", streak) #shows the number of correct streaks
			if streak%2==0 and streak!=0: #for every 2 streaks, gets 2 golds
				w=int(w)+2
				print("You have earned two golds. Gold:", w)
			print()
			print("=============================\n")
			n=input("PRESS ANY KEY TO CONTINUE: ")
			os.system('clear')
			x=x+1 #to increase the length of the pattern by 1
			if long_streak<streak:  #sets the longest streak of correct answers
				long_streak=streak
			streak=streak+1
			
def file_handle(x): #(high_score) (all names in highscore dictionary are accessed here that's why it is 'write' instead of 'append')
	fH=open("scores.txt", "w")
	for k in x.keys():
		iskor=x[k]
		fH.write(str(k)+","+str(iskor[0])+","+str(iskor[1])+","+str(iskor[2])+","+str(iskor[3])+","+"\n")
	fH.close()

def scorestxt(): #to create an empty file if the file DNE and also to not overwrite the saved scores
	fH=open("scores.txt", "a")
	fH.write("")
	fH.close()

def load_scores(): #accesses each line of scores in the file 
	value=[]
	fh=open("scores.txt", "r")
	for line in fh:
		data=line.split(",")
		data[1]=float(data[1]) #float because score can be multiplied by multipier(1.5)
		data[3]=int(data[3])
		value.append(data)
		high_score[data[0]]=[data[1],data[2],data[3],data[4]]
	fh.close()
	return high_score


gold=0 #form of currency used to buy powerups
plus_lives=0 #powerup that adds one to the original lives(3) of the game
multiplier=1 #powerup that multiplies the score by 1.5x


def gold():
	goldFile=open("gold.txt", "a") #to create an empty file if the file DNE and also to not overwrite the saved no. of golds  
	goldFile.write("")
	goldFile.close()
 
def load_gold():  #to access the gold
	goldFile=open("gold.txt", "r") 
	if goldFile!="":
		for line in goldFile:
			gold=line
			return gold
	else:
		return None
gold() 
gold=load_gold()
if gold==None:
	gold=0


while True:
	gold=int(gold)
	choice=Menu(gold)
	scorestxt()         
	final=load_scores()   #load the scores
	if choice==1:
		name=input("Please enter your name: ")
		time.sleep(0.5)
		print()
		print("Welcome",name,"!")
		print("Select difficulty: \n")
		print("[1] Easy")
		print("[2] Medium")
		print("[3] Hard")
		print("[4] Back")
		print()
		difficulty=int(input("Please enter a number: "))

		if difficulty==1:
			c=4  #starting length of pattern in easy      #used in creating pattern
			alpha="abcdefghijklmnopqrstuvwxyz"            #used in creating pattern
			z=len(alpha)-1                                #used in creating pattern
			points=game(c,alpha,z,gold,plus_lives,multiplier)
			gold=points.pop(3) #Removes the gold in the list(so that it wont appear on the leaderboeards) and also updates the value of gold                                     
			high_score[name]=points + ["Easy"]
			file_handle(high_score)		

		elif difficulty==2:
			c=5  #starting length of pattern in medium
			alpha="a0bc1de2fgh3ij4klm5nop6qr7stu8vwx9yz"
			z=len(alpha)-1
			points=game(c,alpha,z,gold,plus_lives,multiplier)
			gold=points.pop(3)
			high_score[name]=points + ["Medium"]
			file_handle(high_score)
			
		elif difficulty==3:
			c=6
			alpha="Aa0BbCc1DdEe2FfGgHh3IiJj4KkLlMm5NnOoPp6QqRr7SsTtUu8VvWwXx9YyZz"
			z=len(alpha)-1
			points=game(c,alpha,z,gold,plus_lives,multiplier)
			gold=points.pop(3)
			high_score[name]=points + ["Hard"]
			file_handle(high_score)
			
	elif choice==2:
		if final=={}:
			print()
			print("Loading scores....\n")
			time.sleep(2)
			print("No Scores Yet!")
		else:
			print("Loading scores....\n")
			time.sleep(2)
			print("======High Scores======")
			print("Rank     Name     Score     Last Pattern     Difficulty     Longest Streak")      
			sort=sorted(final.items(), key=lambda x:x[1][0], reverse=True)  #Used to sort the the score from highest to lowest.Used lambda as key to get the values of the final.items()                          
			c=1                                                             #Used x:x[1][0] since the index of the score is [1][0]                       
			for i in sort:
				print(c,"     ",i[0],"     ",i[1][0],"     ",i[1][1],"     ",i[1][3],"     ",i[1][2])
				c=c+1

	elif choice==3:
		if high_score=={}:
			print()
			print("Scores are not yet available")
		else:
			print()
			print("Deleting scores...\n")
			time.sleep(2)
			final.clear() #clears the data in the scores
			fH=open("scores.txt", "w") #clears the data in the file
			fH.write("")
			fH.close()
			print("All scores are deleted")

	elif choice==4:
		while True:
			print("=====Purchase Powerups=====\n")
			print("Gold:", gold)
			print("[1] Buy Additional Lives")
			print("[2] Buy Score Multiplier")
			print("[3] Coming Soon")
			print("[4] Back")
			buy=int(input("Select a powerup: "))
			print("============================\n")
			if buy==1:
				print("Costs 6 golds. Continue?")
				print("[1] Yes")
				print("[2] No\n")
				add_lives=int(input("Select a number: "))
				if add_lives==1:
					print()
					if int(gold)>=6:
						print("Additional 1 life purchased. The life will be used in the next game\n")
						gold=gold-6
						plus_lives=plus_lives+1
					else:
						print("Gold not sufficient\n")
			elif buy==2:
				print("Costs 9 golds. Continue?\n")
				print("[1] Yes")
				print("[2] No\n")
				score_multiply=int(input("Select a number: "))
				if score_multiply==1:
					print()
					if int(gold)>=9:
						print("You have now purchased 1.5x score multiplier. The multiplier will take effect in the next game\n")
						gold=gold-9
						multiplier=1.5
					else:
						print("Gold not sufficient\n")
			elif buy==3:
				print("The powerup is under development\n")
			elif buy==4:
				break

	elif choice==5:
		print()
		print("The game prints a randomly generated pattern")
		print("and then clears the screen after some amount of time.")
		print("You have to type the pattern correctly until you answered incorrectly.")
		print("You are only allowed to have 3 mistakes unless you have powerups.")
		print("2 golds are given for every 2 streaks")
		print("Goodluck!\n")
		time.sleep(4)

	elif choice==6:
		print("Goodbye!")
		break

	gold=str(gold)

	goldFile=open("gold.txt", "w") #stores the gold in this file
	goldFile.write(gold)
	goldFile.close()

