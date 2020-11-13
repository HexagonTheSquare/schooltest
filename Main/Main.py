#Imports
from datetime import datetime, timedelta
import os.path
import random

#Global declarations (declaring variables I'll use over multiple functions)
now = datetime.now()
current_time = now
lastDay = now
idsEaten = []

#Constants (variables that never change)
_filename = "elever.txt"
_lunch_time = now.replace(hour=11, minute=00)
_lunch_period = now.replace(hour=13, minute=00)

#Functions
def CheckStatus(id):
    if isLunchTime() and not id in idsEaten:
        print("Enjoy your meal!")

        #If you want to be proper, I would save this in another .txt file that resets everyday, so that the data is retained even if the program resets
        idsEaten.append(id)
    elif not isLunchTime():
        print("Sorry, it's not lunchtime!")
    elif id in idsEaten:
        print("You've already eaten!")

def isLunchTime():
    now = datetime.now()

    if now.hour >= _lunch_time.hour and now.hour <= _lunch_period.hour:
        return True
    else:
        return False

def CurrentTime():
    if now.hour > 16:
        return("Good evening")
    elif now.hour < 12:
        return("Good morning")
    else:
        return("Good afternoon")


#Check if file exists, if not we create one
if os.path.exists(_filename) == False:
    print(_filename + " not found, generating file (numbers above 10k can take a while)")

    #Set lastDay as yesterday because lastday has never been set before
    lastDayTemp = now - timedelta(days=1)
    lastDay = lastDayTemp
    with open(_filename, "w+") as f:

        #Generation of 300 random students with unique ID's
        firstNames = ["Elias","Karam","Lukas","Mikael","Anders","Viktor","Robert","Erik","Ludvig","Aaron","Jacob","Kavin","Albin","Hans","Amanda","Emilia","Cecilia","Elsa"]
        lastNames = ["Singh","Eriksson","Breji","O'Leary","McManner","Ulfsson","Lindqvist","Lund","Törne","Von Rosen","Von Bolton","Ekblad","Törnqvist","Kabilan"]
        
        for x in range(0,300):

            #Get random first and last name by generating random index (-1 because by default len() is 1 longer than max index)
            firstName = firstNames[random.randint(0,len(firstNames)-1)]
            lastName = lastNames[random.randint(0,len(lastNames)-1)]

            #Loop through number generation until number is unique (not very time efficient but it works)
            number = 0
            numberGenerating=True
            while numberGenerating:

                #Generate number as string to allow it to be searched for and written
                number = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
                with open(_filename) as b:
                    if not number in b:
                        numberGenerating=False

            #Write generated name in the text file
            f.write(firstName + " " + lastName + ":" + number + "\n")
        print("File generation("+_filename+") is complete!")
        
#If today is a new day, reset who has already eaten
if lastDay.day<now.day:
    idsEaten = []


#Begin loop for main program
running = True
with open(_filename,"r") as x:
    print("Insert Student ID to get your ticket. Type exit to exit")
    while running:
        #Seek() resets the file cursor to the top, so we don't have to load the file for every loop
        x.seek(0)
        num = str(input("Student ID:"))
        if num == "Exit" or num == "exit":
            running=False

        #Check if ID is in file 
        for line in x:
            if num in line:
                
                #Seperates the line by the ":" so for example Jonas Rosenqvist:375 would turn into a list with the value: name = [Jonas Rosenqvist, 375]
                name = line.split(":")
                
                #Gives a welcome message dependent on time (Good evening, etc) + the first value of the list we just created, which is the name, and then prints it.
                print(CurrentTime()+", "+name[0]+"!")
                CheckStatus(num)



                
#                      __________           ___ ___                                                                               
#                      \______   \___.__.  /   |   \   ____ ___  ________     ____   ____   ____                                  
#                       |    |  _<   |  | /    ~    \_/ __ \\  \/  /\__  \   / ___\ /  _ \ /    \                                 
#                       |    |   \\___  | \    Y    /\  ___/ >    <  / __ \_/ /_/  >  <_> )   |  \                                
#                       |______  // ____|  \___|_  /  \___  >__/\_ \(____  /\___  / \____/|___|  /                                
#                              \/ \/             \/       \/      \/     \//_____/             \/                                 
                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                
                                                                                                                                
                                                                                                                                
#   ________                  .___ .__                 __                       __  .__               __                   __  ._.
#  /  _____/  ____   ____   __| _/ |  |  __ __   ____ |  | __   ____   ____   _/  |_|  |__   ____   _/  |_  ____   _______/  |_| |
# /   \  ___ /  _ \ /  _ \ / __ |  |  | |  |  \_/ ___\|  |/ /  /  _ \ /    \  \   __\  |  \_/ __ \  \   __\/ __ \ /  ___/\   __\ |
# \    \_\  (  <_> |  <_> ) /_/ |  |  |_|  |  /\  \___|    <  (  <_> )   |  \  |  | |   Y  \  ___/   |  | \  ___/ \___ \  |  |  \|
#  \______  /\____/ \____/\____ |  |____/____/  \___  >__|_ \  \____/|___|  /  |__| |___|  /\___  >  |__|  \___  >____  > |__|  __
#         \/                   \/                   \/     \/             \/             \/     \/             \/     \/        \/