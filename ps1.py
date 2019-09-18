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
    flag=0   
    for x in range(0,len(par_data)):
        trans_data.append(par_data[x])
        flag=flag+1
        if flag >=3:  #
            if par_data[x]=='0' and par_data[x-1]=='1' and par_data[x-2]=='0':
                trans_data.append('0')
                flag=0            

    return trans_data
        
            

def main():
    input_data = input("enter binary data: ")
    input_list = list(input_data)   
    parity_bit_data = parity(input_list)
    print("Parity bit data: ",''.join(parity_bit_data))
    transmit_data = orient_bit(parity_bit_data)
    transmit_data.append('0101')
    print("Transmitting data: ",''.join(transmit_data))
                    
        
if __name__== "__main__":
  main()


