import os,platform,threading,time,random

#--Inital Vars--#
Hunger = random.randint(60,100) 
Thirst =  random.randint(60,100) 
Happiness = random.randint(60,100) 
petName = 'unnamed'
systemClear = 'undetermined'
#----#

#--Checks System for clear function called later--#
def systemCheck():
    global systemClear

    if platform.system() == 'Windows':
        systemClear = 'cls'
        nameConf()
    else:
        systemClear = 'clear'
        nameConf()

#--Name configuration function--#
#-Starts Threading for stat drain-#
def nameConf():
    global petName
    petName = input('What is Your pets name?\n')
    print(f'your pets name is {petName}')

    nameWrong = input('is this correct?\n 1) Yes/Y\n 2) No/N\n')

    if nameWrong.lower() in ('yes','y','1'):
        print('this is correct')
        thread = threading.Thread(target=statDrain, daemon=True)
        thread.start()
        mainPetFunc()

    else:
        nameConf()

#--Main Interaction with pet--#
def mainPetFunc():
    global petName

    os.system(systemClear)
    print('your pet stats:\n'
        f'Name:{petName}\n'
        f'Hunger:{Hunger}\n'
        f'Thirst:{Thirst}\n'
        f'Happiness:{Happiness}\n')
    
    intrctOpt = input('What would you like to do?\n1) Feed\n 2) Water\n 3)Pet\n 4)Play\n')
    
    if intrctOpt.lower() in ['feed','1']:
        feedFunc()
    
    else:
        print('Input valid interaction')
        time.sleep(1)
        mainPetFunc()
#--Function that controls feeding--#
def feedFunc():
    global Hunger 
    os.system(systemClear)
    foodOpt = input('What would you like to feed your pet?\n 1) Cake\n 2) Burger and Fries\n 3) Chicken Alfredo\n 4) Salad\n')
    foodOpt = foodOpt.lower()

    if foodOpt in  ['1','cake']:
        Hunger += random.randint(3,12)
        print('fed cake')
        time.sleep(5)
        mainPetFunc()
    
    elif foodOpt in ['2','burger and fries','burger','fries']:
        Hunger += random.randint(5,10)
        print('fed burger')
        time.sleep(5)
        mainPetFunc()
    elif foodOpt in ['3','chicken','alfredo','chicken Alfredo']:
        Hunger += random.randint(10,15)
        print('fed Chicken')
        time.sleep(5)
        mainPetFunc()

    elif foodOpt in ['4','salad']:
        Hunger += random.randint(1,5)
        print('fed salad')
        time.sleep(5)
        mainPetFunc()

    else:
        os.system(systemClear)
        print('Input a food choice!')
        feedFunc()

#--Threading function for stat drains--#
def statDrain():
    global Hunger
    global Thirst
    global Happiness
    
    print('now threading')
    randStat = random.randint(1,3)
    randAmt = random.randint(1,5)

    while True:
        if randStat == 1:
            if Hunger > 0:
                Hunger -= randAmt
                #print('drained Hunger')
            else:
                Hunger == 0

        if randStat == 2:
            if Thirst > 0:
                Thirst -= randAmt
                #print('drained Thirst')                
            else:
                Thirst == 0
        if randStat == 3:
            if Happiness > 0:
                Happiness -= randAmt
                #print('drained Happiness')
            else:
                Hunger == 0
        time.sleep(10)
        randStat = random.randint(1,3)
        randAmt = random.randint(1,5)

systemCheck()

    


