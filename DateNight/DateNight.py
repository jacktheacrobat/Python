money = 150
time = 3
haveEaten = False

#prints the current time and amount of money remaining
def getTimeandMoney():
    global money, time
    print ("You have"), money, ("dollars remaining.")
    print ("It is now"), time, ("o-clock.")

#Logical tree of food selection based on food budget
def get_food():
    global money, time, haveEaten
    foodBudget = input("How much money are you willing to spend on food? (You only have $150 available)")
    #Food at Da Vinci's
    if foodBudget >= 110:
        print ("Get food at Da Vinci's for $110")
        money -= 110
        time += 2
        haveEaten = True
    #Food at Fukiyama Sushi
    elif foodBudget < 110 and foodBudget >= 80:
        print ("Get food at Fukiyama Sushi for $80")
        money -= 80
        time += 2
        haveEaten = True
        #Food at Fancy-Dogs
    elif foodBudget < 80 and foodBudget >= 30:
        print ("Get food at Fancy-Dogs for $30")
        money -= 30
        time += 2
        haveEaten = True
        #Food at Ten Guys
    else:
        print ("Get food at Ten Guys for $25")
        money -= 25
        time += 2
        haveEaten = True
    getTimeandMoney()

#Logic tree of activities based on current time and amount of money remaining
def doActivity():
    global money, time
    while time < 12:
        #Go to Shakespeare
        if time <= 4 and money >= 45:
            print ("Go see Shakespeare in the park for $45 from 4-6pm")
            money -= 45
            time = 6
        #Either go skating or see a movie
        elif time <= 7:
            if money < 65:  #cannot afford movie // Select number of hours to go skating for
                selection = 0
                while selection != 1 or selection != 2:
                    print ("Go skating for free")
                    selection = input("Enter the number of hours you would like to skate for (up to 3hrs)")
                    if selection == 1:
                        print ("Go skating for free from 7-8pm")
                        money -= 0
                        time = 8
                        getTimeandMoney()
                        break
                    elif selection == 2:
                        print ("Go skating for free from 7-9pm")
                        money -= 0
                        time = 9
                        getTimeandMoney()
                        break
                    elif selection >= 3:
                        print ("Go skating for free from 7-10pm")
                        money -= 0
                        time = 10
                        getTimeandMoney()
                        break
                    else:
                        print ("That was an invalid entry, please try again")
            #Decide between skating and movie
            else:
                selection = 0
                while selection == 0:
                    selection = input("Enter 1 to skate for free from 7-10pm, or Enter 2 to watch a movie for $65 from 7-9pm")
                    #Go skating
                    if selection == 1:
                        print ("Go skating for free from 7-10pm")
                        money -= 0
                        time = 10
                        getTimeandMoney()
                        break
                    #See a movie
                    elif selection == 2:
                        print ("Go see a movie for $65 from 7-9pm")
                        money -= 65
                        time = 9
                        getTimeandMoney()
                        break
                    #Bad entry
                    else:
                        print ("That was an invalid entry, please try again")
        #Go bowling
        elif time <= 9 and money >= 30:
            print ("Go bowling for $30 from 9-12am")
            money -= 30
            time = 12
        #Go for a boat ride
        elif time <= 10 and money >= 70:
            print ("Go for a boat ride for $70 from 10-12am")
            money -= 70
            time = 12             
    getTimeandMoney()

#Allows user to select whether to plan another date
def scheduleDate():
    selection = 0
    while selection != 1 or selection != 2:
        selection = input("Would you like to schedule another date? 1) yes 2) no")
        #Schedule another date
        if selection == 1:
            print ("You have scheduled another date!")
            return 
        #No more dates
        elif selection == 2:
            print ("You decided not to schedule another date.")
            return 
        else:
            print ("That was an invalid entry, please try again")

#Start MAIN
if (haveEaten == False):
    get_food()
doActivity()
scheduleDate()

print ("I hope you had a had fun!")
print ("Goodbye")
