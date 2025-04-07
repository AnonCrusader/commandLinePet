import os
import platform
import threading
import time

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


systemCheck()

    


