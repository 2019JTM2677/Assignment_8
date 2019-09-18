# program for Problem statement-1
import math
def parity(input_lis):      #function to get parity bit
    count=0
    par_list= input_lis
    for bit in input_lis:  #counting no of 1's 
            if(bit=='1'):
                count+=1
    parity_bit='0'
    if count%2==0:
        parity_bit='1'
    par_list.append(parity_bit)
    return par_list
    
  

def orient_bit(par_data): #Function for bit stuffing
    trans_data=[]
    for i in range(0,3):
        trans_data.append(par_data[i])
    for x in range(3,len(par_data)):
        y=x
        if par_data[x-1]=='0' and par_data[x-2]=='1' and par_data[x-3]=='0':
            trans_data.append('0')
            y+=1

        trans_data.append(par_data[x])
        y+=1
    return trans_data
        
            

def main():
    input_data = input("enter binary data: ")
    input_list = list(input_data)   
   # print(input_list)
    print("Input data",''.join(input_list))
    parity_bit_data = parity(input_list)
    print("Parity bit data: ",''.join(parity_bit_data))
    transmit_data = orient_bit(parity_bit_data)
    transmit_data.append('0101')
    print("Transmitting data: ",''.join(transmit_data))
                    
        
if __name__== "__main__":
  main()


