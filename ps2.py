# program for Problem statement-2

import math

  
     

def main():
    print("Welcome to the Game!")
    flag=1
    while True:
        if flag:
            print("Player 1's chance")
            flag=~flag
        if not flag:
            print("Player 2's chance")
            flag=~flag

        print("Enter the position and number to be entered: ")
        in_string = [int(x) for x in input().split(',')]
        position=in_string[0]
        number=in_string[1]
        print(position,number)
        
        if position not in range(1,10) or number not in range(1,10):
            print("Please enter valid number and position")
            exit(1)
        col=row=3
        tic_tac = [['\0' for i in range(col)] for j in range(row)] 
        print(tic_tac)
        #tic_tac[position-1]=  number        
        
if __name__== "__main__":
  main()
