import random


#creates a person to add to the board
class Person:
    def __init__(self, name, gender, hairColor, eyeColor, shirtColor, hasGlasses, hasEarrings, hairLength):
        self.name=name
        self.gender = gender
        self.hairColor = hairColor
        self.eyeColor = eyeColor
        self.shirtColor=shirtColor
        self.hasGlasses= hasGlasses
        self.hasEarrings = hasEarrings
        self.hairLength = hairLength


#prints out the person to the board
    def __str__(self):
        return (f"Name: {self.name} || Gender: {self.gender} || Hair Color: {self.hairColor} || Eye color: {self.eyeColor} || Shirt Color: {self.shirtColor}  || Has glasses: {self.hasGlasses} || Has earrings: {self.hasEarrings} || Hair Length: {self.hairLength}")


#people
p1 = Person("Johnny", "Male", "Brown","Green","Red","No Glasses", "No Earrings","Short Hair")
p2 = Person("Jenna", "Female", "Blonde","Brown","Yellow","No Glasses", "Earrings","Medium Hair")
p3 = Person("Aiden", "Male", "Brown","Brown","Green","No Glasses", "No Earrings","Long Hair")
p4 = Person("Kayla", "Female", "Brown","Brown","Blue","Glasses", "No Earrings","Short hair")
p5 = Person("Chris", "Male", "Ginger","Blue","Red","No glasses", "earrings","medium hair")
p6 = Person("Emma", "Female", "Brown","Green","Yellow","glasses", "No earrings","long hair")
p7 = Person("Luke", "Male", "Black","Brown","Green"," Glasses", "Earrings","Short Hair")
p8 = Person("Maya", "Female", "Black","Blue","Blue","No glasses", "No earrings","medium hair")
p9 = Person("Jack", "Male", "Black","Green","Red","No glasses", "No earrings","long hair")
p10 = Person("Annie", "Female", "Blonde","Brown","Yellow","glasses", "No earrings","Short hair")
p11= Person("Anna", "Female", "Blonde","Brown","Yellow","Glasses", "Earrings","Long hair")
p12 = Person("Mike", "Male", "Black","Blue","Green"," No Glasses", "No earrings","Short hair")
p13 = Person("Allie", "Female", "Ginger","Brown","Blue"," No Glasses", "No earrings","medium hair")
p14 = Person("Isaac", "Male", "Black","Green","Green","  Glasses", "Earrings","Short hair")
p15 = Person("Eric", "Male", "Blonde","Blue","Red"," No Glasses", "No earrings","Medium hair")
p16 = Person("Alexa", "Female", "Brown","Blue","Red"," No Glasses", "earrings","long hair")
p17 = Person("Maddie", "Female", "Ginger","Brown","Yellow"," No Glasses", "No earrings","long hair")
p18 = Person("Bob", "Male", "Black","Green","Blue"," No Glasses", "No earrings","Short hair")
p19 = Person("Ashley", "Female", "Black","Blue","Green"," No Glasses", "earrings","Short hair")
p20 = Person("James", "Male", "Brown","Green","Yellow"," Glasses", "No earrings","Short hair")


#adds all the possible people to a list
listOfPeople = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12, p13, p14,p15, p16,p17,p18,p19,p20]
#does your character have...
global traits
traits = [
    "Female",
    "Male",
    "Brown Hair",
    "Blonde Hair",
    "Black Hair",
    "Ginger Hair",
    "Green Eyes",
    "Brown Eyes",
    "Blue Eyes",
    "Red Shirt",
    "Yellow Shirt",
    "Green Shirt",
    "Glasses",
    "No Glasses",
    "Earrings",
    "No Earrings",
    "Short Hair",
    "Medium Hair",
    "Long Hair"
]


global userTurns, computerTurns
userTurns = 0
computerTurns = 0


#creates a random list of people for both the user and computer
def createNewGame():
    global gameBoard
    global userGameBoard
    global computerGameBoard
    gameBoard=[]
    global userTurns, computerTurns
    userTurns = 0
    computerTurns = 0
    #add 10 people to the user board
    gameBoard = random.sample(listOfPeople,10)
   
    userGameBoard = gameBoard.copy()
    computerGameBoard = gameBoard.copy()
    #prints out the board
    print("This is your game board, both you and the computer will have to guess a character from this board:")
    printGameBoard(gameBoard)
    selectCharacter()
    startgame()


#select the character that the player and computer have to guess
def selectCharacter():
    global userCharacter
    global computerCharacter
    userCharacter = random.choice(gameBoard) # the character the user has to guess
    computerCharacter = random.choice(gameBoard) # the character the computer has to guess
    print("\nYour character is:", userCharacter.name,"\nThe computer has to guess that this is your character based on this list of people! You have to try to guess the computer's character based on this same list.\n") # the computer has to guess user's character


#this function restarts the game  
def restartingGame():
    k = input("Enter Y to restart the game, or N to quit: ")


    while (k.upper() != "Y" and k.upper()!="N"):
        print("Please enter either Y or N")
        k = input("Enter Y to restart the game, or N to quit: ")


    if (k.upper() == "Y"):
        createNewGame()
    else:
        print("Thanks for playing!")
        exit(0)
   
#this function returns the total number of turns made in a game when it ends  
def stats():
    global userTurns, computerTurns
    print("The computer made", computerTurns, "turns.")
    print("You made", userTurns, "turns.")


#this function lets the user make a guess
def makeGuess(name):
    global userTurns
    userTurns += 1
    #The user is making a guess
    if (name == computerCharacter.name):
        print("Congratulations! You guessed the computer's character correctly and won the game!")
    else:
        print("The guess was incorrect. The game is over.")
        print("The computer's character was:", computerCharacter.name)
        print("Better luck next time!")
    stats()
    restartingGame()


#this function lets the user get a hint about what the best question to ask would be if they don't know what to ask
def getHint():
    n = len(userGameBoard)
    if (n == 1):
        print("There's only one person left. You should guess", userGameBoard[0].name,"to win the game")


    mn = n + 1
    for x in traits:
        # count how many people who have not been eliminated have this trait in computer's game board
        count = 0
        for person in userGameBoard:
            if (x.lower() == "no glasses"):
                if (person.hasGlasses.lower() == "no glasses"):
                    count += 1
            elif (x.lower() == "glasses"):
                if (person.hasGlasses.lower() == "glasses"):
                    count += 1
            elif (x.lower() == "no earrings"):
                if (person.hasEarrings.lower() == "no earrings"):
                    count += 1
            elif (x.lower() == "earrings"):
                if (person.hasEarrings.lower() == "earrings"):
                    count += 1
            elif ("hair" in x.lower()):
                if (person.hairLength.lower() in x.lower() or person.hairColor.lower() in x.lower()):
                    count += 1
            elif ("shirt" in x.lower()):
                if (person.shirtColor.lower() in x.lower()):
                    count += 1
            elif ("eyes" in x.lower()):
                if (person.eyeColor.lower() in x.lower()):
                    count += 1
            elif ("female" in x.lower()):
                count += 1
            elif ("male" in x.lower()):
                count += 1


        dif = abs(n - 2*count)
       
        if (dif < mn):
            mn = dif
            bestTrait = x
            bestCount=count
       
    eliminatedFraction = bestCount/n
    if(bestTrait.lower()=="male"or bestTrait.lower()=="female"):
        print("\nA good question to ask would be: Is your character "+ bestTrait.lower()+"?")
        print("You should ask this question because", bestCount, "people are",bestTrait.lower(), "so the answer to this question could eliminate", f"{eliminatedFraction*100}% of the board.\n")
    else:    
        print("\nA good question to ask would be: Does your character have "+ bestTrait+"?")
        print("You should ask this question because", bestCount, "people have",bestTrait.lower(), "so the answer to this question could eliminate",f"{eliminatedFraction*100}% of the board.\n")
    return 0


#prints the game board to the screen
def printGameBoard(board):
    for i in range(len(board)):
        print((i+1),"--", board[i],"\n")


global id


#updates the board based on a true trait
def updateTrueUserBoard(attribute, trait):
    global userGameBoard
    newBoard= []
    for person in userGameBoard:
        if getattr(person,attribute).lower()==trait.lower():
            newBoard.append(person)
    userGameBoard= newBoard
    print("This is your new game board after eliminations")
    return userGameBoard


#updates the board based on a false trait
def removeFromUserBoard(attribute, trait):
    global userGameBoard
    newBoard = userGameBoard.copy()
    for person in userGameBoard:
        if getattr(person, attribute).lower()==trait.lower():
            newBoard.remove(person)
    userGameBoard= newBoard
    print("This is your new game board after eliminations")
    return userGameBoard


#the user asks a question
def userAskQuestion():
    global userTurns


    while True:
        choice=0
        while choice not in ("1","2","3"):
            choice = input("Would you like to ask the computer's character's gender or something they have?\n Enter 1 for gender, enter 2 for something they have\nIf you're unsure, Enter 3 to get a hint about what the best question to ask would be")
       
        choice = int(choice)


        #adds to the total number of turns the user made in the game if they ask a question
        if choice in (1,2):
            userTurns += 1
            #gender questions
        if choice==1:
            genderChoice=0
            while genderChoice!="1" and genderChoice!="2":
                genderChoice = input(("Select a question for the gender: \n1- Is your character female? \n2-Is your character male?"))
           
            genderChoice = int(genderChoice)
           
            #asks if the computer's character is female
            if genderChoice==1:
                print("You asked the computer Is your character female?")
                if computerCharacter.gender=="Female":
                    print("The computer answered, yes, my character is female")
                    updateTrueUserBoard("gender", "Female")
                    printGameBoard(userGameBoard)
                    return
                else:
                    print("The computer answered no")
                    updateTrueUserBoard("gender", "Male")
                    printGameBoard(userGameBoard)
                    return
            elif genderChoice==2: # asks if the computer's character is male
                   
                if computerCharacter.gender=="Male":
                    print("The computer answered, yes, my character is male")
                    updateTrueUserBoard("gender", "Male")
                    printGameBoard(userGameBoard)
                    return
                else:
                    print("The computer answered no")
                    updateTrueUserBoard("gender", "Female")
                    printGameBoard(userGameBoard)
                    return
            #does your character have __ questions
       
        elif choice==2:
            haveChoice=0
            while haveChoice not in ("1","2","3","4","5","6"):
                haveChoice= input("Select a question to ask if the computer's character has something. \n1- Hair color\n2- Eye color\n3- Shirt Color\n4- Glasses \n5-Earrings \n6-Hair Length")
           
            haveChoice = int(haveChoice)
               
            if haveChoice==1:
                typeChoice=0
                hairOptions = {1:"black",2:"brown", 3:"blonde",4:"ginger"}
                while typeChoice not in ("1","2","3","4"):
                    typeChoice = input(("Select a question to ask about the hair color: Does your character have... \n1-black hair? \n2-brown hair?\n3-blonde hair?\n4-ginger hair?"))
               
                typeChoice = int(typeChoice)
                    #hair color questions
                    #black hair
                chosenColor = hairOptions[typeChoice]
                if computerCharacter.hairColor.lower()==chosenColor.lower():
                    print("The computer answered, yes, my character has", chosenColor,"hair")
                    updateTrueUserBoard("hairColor", chosenColor)
                    printGameBoard(userGameBoard)
                    return
                else:
                    print("The computer answered, no, my character doesn't have",chosenColor,"hair")
                    removeFromUserBoard("hairColor",chosenColor)
                    printGameBoard(userGameBoard)
                    return
                #eye color questions
            elif haveChoice==2:
                typeChoice=0
                eyeOptions = {1:"brown",2:"blue",3:"green"}
                while typeChoice not in ("1","2","3"):
                    typeChoice = input(("Select a question to ask about the eye color: Does your character have... \n1-brown eyes? \n2-blue eyes?\n3-green eyes?"))
               
                typeChoice = int(typeChoice)
               
                chosenColor= eyeOptions[typeChoice]
                if computerCharacter.eyeColor.lower()==chosenColor.lower():
                    print("The computer answered, yes, my character has", chosenColor,"eyes")
                    updateTrueUserBoard("eyeColor", chosenColor)
                    printGameBoard(userGameBoard)
                    return    
                else:
                    print("The computer answered, no, my character doesn't have",chosenColor,"eyes")
                    removeFromUserBoard("eyeColor",chosenColor)
                    printGameBoard(userGameBoard)
                    return
       
            #Shirt color questions
            elif haveChoice==3:
                typeChoice=0
                shirtOptions = {1:"Red",2:"Yellow",3:"Green",4:"Blue"}
                while typeChoice not in ("1","2","3","4"):
                    typeChoice = input(("Select a question to ask about the shirt color: Does your character have... \n1-red shirt? \n2-yellow shirt?\n3-green shirt?\n4-blue shirt"))
                typeChoice = int(typeChoice)
                chosenColor= shirtOptions[typeChoice]
                if computerCharacter.shirtColor==shirtOptions[typeChoice]:
                    print("The computer answered, yes, my character has a", chosenColor, "shirt")
                    updateTrueUserBoard("shirtColor", chosenColor)
                    printGameBoard(userGameBoard)
                    return
                else:
                    print("The computer answered, no, my character doesn't have a", chosenColor,"shirt")
                    removeFromUserBoard("shirtColor",chosenColor)
                    printGameBoard(userGameBoard)
                    return  
            #has glasses questions
            elif haveChoice==4:
                print("You asked the computer Does your character have glasses?")
                if computerCharacter.hasGlasses.lower()=="no glasses".lower():
                        print("The computer answered, no, my character does not have glasses")
                        removeFromUserBoard("hasGlasses", "Glasses")
                        printGameBoard(userGameBoard)
                        return
                else:
                    print("The computer answered, yes, my character has glasses")
                    updateTrueUserBoard("hasGlasses","Glasses")
                    printGameBoard(userGameBoard)
                    return
       
            #has earrings questions
            elif haveChoice==5:
                print("You asked the computer Does your character have earrings?")
                if computerCharacter.hasEarrings.lower()=="no earrings".lower():
                    print("The computer answered, no, my character does not have earrings")
                    removeFromUserBoard("hasEarrings", "Earrings")
                    printGameBoard(userGameBoard)
                    return
                else:
                    print("The computer answered, yes, my character has earrings")
                    updateTrueUserBoard("hasEarrings","Earrings")
                    printGameBoard(userGameBoard)
                    return


            #hair length questions
            if haveChoice==6:
                typeChoice=0
                lengthOptions= {1:"short hair",2:"medium hair",3:"long hair"}
                while typeChoice not in ("1","2","3"):
                    typeChoice = input("Would you like to ask the computer if their character has... \n1-short hair\n2-medium hair\n3-long hair")
               
                typeChoice = int(typeChoice)
                print("typechoice", typeChoice)
                chosenLength = lengthOptions[typeChoice]
               
                print("You asked the computer Does your character have",chosenLength, "hair?")
                if computerCharacter.hairLength.lower()==chosenLength.lower():
                    print("The computer answered, yes, my character has",chosenLength, "hair")
                    updateTrueUserBoard("hairLength", chosenLength)
                    printGameBoard(userGameBoard)
                    return
                else:
                    print("The computer answered, no, my character does not have", chosenLength ,"hair")
                    removeFromUserBoard("hairLength",chosenLength)
                    return
                       
       
        elif choice==3:
            getHint()


#this function represents the computer's turn
def computersTurn():
    global computerTurns
    computerTurns += 1


    print("It's the computer's turn!")
    n = len(computerGameBoard)
    if (n == 1):
        print("The computer has correctly guessed your character as:", computerGameBoard[0].name)
        print("The computer wins!")
        stats()
        restartingGame()


    mn = n + 1
    print("number of people left for computer to choose from:", n)


    for x in traits:
        # count how many people who have not been eliminated have this trait in computer's game board
        count = 0
        for person in computerGameBoard:
            if (x.lower() == "no glasses"):
                if (person.hasGlasses.lower() == "no glasses"):
                    count += 1
            elif (x.lower() == "glasses"):
                if (person.hasGlasses.lower() == "glasses"):
                    count += 1
            elif (x.lower() == "no earrings"):
                if (person.hasEarrings.lower() == "no earrings"):
                    count += 1
            elif (x.lower() == "earrings"):
                if (person.hasEarrings.lower() == "earrings"):
                    count += 1
            elif ("hair" in x.lower()):
                if (person.hairLength.lower() in x.lower() or person.hairColor.lower() in x.lower()):
                    count += 1
            elif ("shirt" in x.lower()):
                if (person.shirtColor.lower() in x.lower()):
                    count += 1
            elif ("eyes" in x.lower()):
                if (person.eyeColor.lower() in x.lower()):
                    count += 1
            elif ("female" in x.lower()):
                count += 1
            elif ("male" in x.lower()):
                count += 1


        dif = abs(n - 2*count)
       
        if (dif < mn):
            mn = dif
            bestTrait = x
            bestCount=count
       
    eliminatedFraction = bestCount/n
    if(bestTrait.lower()=="male"or bestTrait.lower()=="female"):
        print("The computer asks: Is your character "+ bestTrait.lower()+"?")
        print("The computer asks this question because", bestCount, "people are",bestTrait.lower(), "so the answer to this question could eliminate",f"{eliminatedFraction*100}% of the board.\n")


    else:    
        print("The computer asks: Does your character have "+ bestTrait+"?")
        print("The computer asks this question because", bestCount, "people have",bestTrait.lower(), "so the answer to this question could eliminate",f"{eliminatedFraction*100}% of the board.\n")
   
    print("\nYOUR CHARACTER: ")
    print(userCharacter)
    answer = input("Enter Y for yes, N for no: ")


    while (answer.upper() != "Y" and answer.upper() != "N"):
        print("Please enter either Y or N")
        answer = input("Enter Y for yes, N for no: ")
        continue


    oldlen = len(computerGameBoard)


    for i in range(len(computerGameBoard)-1, -1, -1):
        person = computerGameBoard[i]
        hasTrait = False
        if (bestTrait.lower() == "no glasses"):
            if (person.hasGlasses.lower() == "no glasses"):
                hasTrait = True
        elif (bestTrait.lower() == "glasses"):
            if (person.hasGlasses.lower() == "glasses"):
                hasTrait = True
        elif (bestTrait.lower() == "no earrings"):
            if (person.hasEarrings.lower() == "no earrings"):
                hasTrait = True
        elif (bestTrait.lower() == "earrings"):
            if (person.hasEarrings.lower() == "earrings"):
                hasTrait = True
        elif ("hair" in bestTrait.lower()):
            if (person.hairLength.lower() in bestTrait.lower() or person.hairColor.lower() in bestTrait.lower()):
                hasTrait = True
        elif ("shirt" in bestTrait.lower()):
            if (person.shirtColor.lower() in bestTrait.lower()):
                hasTrait = True
        elif ("eyes" in bestTrait.lower()):
            if (person.eyeColor.lower() in bestTrait.lower()):
                hasTrait = True
        elif ("female" in x.lower()):
                hasTrait = True
        elif ("male" in x.lower()):
                hasTrait = True
        if (hasTrait and answer.lower() == "n"):
            del computerGameBoard[i]
        elif (not hasTrait and answer.lower() == "y"):
            del computerGameBoard[i]
           
    newlen = len(computerGameBoard)
    print("\nThe computer eliminated", oldlen - newlen, "characters. This is the computer's new game board after elimiations")


    for person in computerGameBoard:
        print(person)
   
    n = len(computerGameBoard)
    if (n == 1):
        print("The computer has correctly guessed your character as:", computerGameBoard[0].name)
        print("The computer wins!")
        stats()
        restartingGame()


    return 0


def userTurn():
    guessOrQuestion=0
    while guessOrQuestion!="1" and guessOrQuestion!="2":
        guessOrQuestion = input("\nIt's your turn! Enter 1 to Ask a Question and Enter 2 to Make a guess")
   
    guessOrQuestion = int(guessOrQuestion)
    if guessOrQuestion==1:
        userAskQuestion()
    elif guessOrQuestion==2:
        person = input("Enter the name of the person you want to guess is the computer's character: ")
        makeGuess(person)
    else:
        print("Please enter either 1 or 2")


def startgame():
    global id
    id = 0
    while (True):
        if (id == 0):
            computersTurn()
        else:
            userTurn()
        id = 1 - id


#main
createNewGame()

