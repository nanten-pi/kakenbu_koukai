import motor
import time
import sys
comand = input("ModeSerct plz 1... active mode 2... edit mode 3... check mode ")
while True :

    if comand == '1':
        activiater = input("plz set what program want you move?")
        if activiater == '1':
            motor.type1
            print('check')
        elif activiater == '2':
            motor.type2
            print('check')
        elif activiater == '3':
            motor.type3
            print('check')
        elif activiater == '4':
            motor.type4
            print('check')
        elif activiater == '5':
            motor.type5
            print('check')
        elif activiater == '6':
            motor.type6
            print('check')
        elif activiater == '7':
            motor.type7
            print('check')
        elif activiater == '8':
            motor.type8
            print('check')
        elif activiater == '9':
            motor.type9
            print('check')
        elif activiater == '10':
            motor.type10
            print('check')
        elif activiater == '11':
            motor.type11
            print('check')
        elif activiater == '12':
            motor.type12
            print('check')
        elif activiater == '13':
            motor.type13
            print('check')
        elif activiater == '14':
            motor.type14
            print('check')
        elif activiater == '15':
            motor.type15
            print('check')
        elif activiater == '16':
            motor.type16
            print('check')
        elif activiater == '17':
            motor.type17
            print('check')
        elif activiater == '18':
            motor.type18
            print('check')
        else:
            print('please enter Ctrl+C and reboot program')
    elif comand == '2':
        print("edit mode")
    elif comand == '3':
        print("it is check mode ")
        checkselect = input("what module do you want to check?")
    else:
        print("Invalid command please check again")
        comand = input("ModeSerct plz 1... active mode 2... edit mode 3... check mode ")
