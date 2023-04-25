QNumber = 8
Username = input("Enter a username.")
Score = 0
HighScore = Score

Difficulty = input("Easy or Hard mode?")
if Difficulty == "Easy":
 Q1 = True 
 Q2 = True
 Q3 = True
 Q4 = True
 Q5 = True
 Q6 = True
 Q7 = True
 HighScore = True
if Difficulty == "Hard":
 Q1 = True
 Q2 = False 
 Q3 = False
 Q4 = False
 Q5 = False
 Q6 = False
 Q7 = False
 HighScore = False

A1 = input("What is the capital of Spain?")
if A1 == "Madrid":
 print("Correct")
 Q2 = True
 Score += 1
else:
 Q2 = False
if Q2 == "False":
 print("Wrong")
 quit()
 
A2 = input("What country is Toronto in?")
if A2 == "Canada":
 print("Correct")
 Score += 1
 Q3 = True
 Score += 1 
else:
 Q2 = False
if Q3 == False:
 print("Wrong")
 quit()
 
A3 = input("What tectonic plate is the UK on?")
if A3 == "Eurasia":
 print("Correct")
 Score += 1
 Q4 = True
else:
 Q4 = False
if Q4 == False:
 print("Wrong")
 quit()
 
A4 = input("How many countries are there?")
if A4 == "195":
 print("Correct")
 Score += 1
 Q5 = True
else:
 Q5 = False
if Q5 == False:
 print("Wrong")
 quit()

A5 = input("What is the highest peak on earth?")
if A5 == "Everest":
 print("Correct")
 Score += 1
 Q6 = True
else:
 Q6 = False
if Q6 == False:
 print("Wrong")
 quit()

A6 = input("What is the biggest waterfall in the world?")
if A6 == "Niagra Falls":
 print("Correct")
 Score += 1
 Q7 = True
else:
 Q7 = False
if Q7 == False:
 print("Wrong")
 quit()
 
A7 = input("What counry's capital is Riga?")
if A7 == "Latvia":
 print("Correct")
 Score += 1
 Q8 = True
else:
 Q8 = False
if Q8 == False:
 print("Wrong")
 quit()

if HighScore == True:
 if Score > HighScore:
 HighScore = Score
 print("Congratulations, you have set a new high score of", HighScore)
else:
 print(Username, "you scored", Score, "out of", QNumber)
