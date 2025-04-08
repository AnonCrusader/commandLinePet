import os
import platform
import threading
import time
import random

#--Basic needs Stats--#
Hunger = 100
Thirst = 100
Happiness = 100
#----#

petName = 'unnamed'
systemClear = 'Undetermined'

def systemCheck():
    global systemClear

    if platform.system() == 'Windows':
        systemClear = 'cls'
        nameConf()
    else:
        systemClear = 'clear'
        nameConf()


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

def mainPetFunc():
    global petName

    os.system(systemClear)
    print('your pet stats:\n'
        f'Name:{petName}\n'
        f'Hunger:{Hunger}\n'
        f'Thirst:{Thirst}\n'
        f'Happiness:{Happiness}\n')
    
    intrctOpt = input('What would you like to do?\n1) Feed\n 2) Water\n 3)Pet\n 4)Play\n')
    



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
                print('drained Hunger')
            else:
                Hunger == 0

        if randStat == 2:
            if Thirst > 0:
                Thirst -= randAmt
                print('drained Thirst')                
            else:
                Thirst == 0
        if randStat == 3:
            if Happiness > 0:
                Happiness -= randAmt
                print('Drained Happiness')
            else:
                Hunger == 0
        time.sleep(10)
        randStat = random.randint(1,3)
        randAmt = random.randint(1,5)

systemCheck()

    


