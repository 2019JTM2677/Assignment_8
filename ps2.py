# program for Problem statement-2

import math

def main():
    print("Welcome to the Game!")
    
    
    flag=1
    player=""
    while (True):
        
        if flag:
            player="Player1"
            print("Player 1's chance")
            flag=0

        else:
            player="Player2"
            print("Player 2's chance")
            flag=1

        print("Enter the position and number to be entered: ")
        in_string = [int(x) for x in input().split(',')]
        position=in_string[0]
        number=in_string[1]
        print(position,number)
        if position not in range(1,10) or number not in range(1,10):
            print("Please enter valid number and position")
            exit(1)
        tic_tac = [' ' for i in range(0,9)]
        tic_tac [position-1]=  number
        for i in range(3):
            print(tic_tac[i*3:(i+1)*3])
            
        #if player =="Player1"

        
if __name__== "__main__":
  main()
        

