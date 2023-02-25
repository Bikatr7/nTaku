import os

from time import sleep

nput = ""
Sum = 0

while(0 == 0):

    nput = input()
    if(nput == "q"):
        exit()
    elif(nput ==""):
        Sum = 0
        os.system('cls')
    elif(nput.isdigit()):
        os.system('cls')
        Sum += int(nput)
        print(Sum)
    else:
        pass


    
