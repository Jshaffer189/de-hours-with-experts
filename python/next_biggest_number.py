#!/usr/bin/python3
import sys

def main():
    next_biggest_number("45071")


def next_biggest_number(num):

    # turn string to integer
    num_map = map(int, num)

    # turn number to a list
    num_list = list(num_map)

    # check if numer cannot be reduced 
    if sorted(num_list, reverse=True) == num_list:
        return -1

    test_number = 

    # loop in reverse and check if any numbers can be rearranged
    for n in reversed(range(len(num_list))):
        # if right most digit is bigger then next digit then return a swap number 
        # num_list[n - 1]
        if num_list[n] > test_number:
            
            num_list[n], num_list[n - 1] = num_list[n - 1], num_list[n]
            
            return print(num_list)

        
        



            #print("bigger", num_list[n], num_list[n - 1])
        #else:
            #print("smaller", )
            
        

 







    



   

if __name__ == "__main__":
    main()



