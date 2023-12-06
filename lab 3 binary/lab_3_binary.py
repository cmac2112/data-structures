# Test Sorts and Searches
# programmer: Leroy Wilson
# Date: 9/1/2022

from operator import index, indexOf
import time
import random
# This program generates random numbers. The numbers will be sorted
# and  particular number will be searched.

# main definition
def main():

    num = 100  # random numbers to generate, ask for input for larger numbers
    xnumlist = []  # List to hold random numbers

    # Generate random numbers and add them to the a list
    for x in range(num):
        x = random.randint(1000000, 9999999)
        xnumlist.append(x)

    # sort the data
    selectionSort(xnumlist)

    # Get a random number in list to be search for test purposes
    numx =  random.randint(0, num)
    print(f" For test purposes only: {xnumlist[numx]}")
    print(xnumlist)

    # enter an number to be searched.
    inputAnswer = int(input('Enter a number to be searched: '))
    start = time.time()   # Start time
    # Determine if number is found
    

    result = binarysearch(xnumlist, 0, len(xnumlist)-1, inputAnswer)
    print('bru')
    print(result)
    end = time.time()
    # print the difference between start
    # and end time in milli. secs
    print()
    print("The time of execution of above program is :",(end - start), "ms") #numbers are too small to round in milliseconds

# Swap Function to exchange items in a list
def swap(wlist, i, j):
    # Exchange the items at positions i and j.
    temp = wlist[i]
    wlist[i] = wlist[j]
    wlist[j] = temp


# This function will sort the incoming list of numbers
# from the min to the max number.
def selectionSort(wlist):

    for i in range(len(wlist)): # loop though each item in the list
        minIndex = i
        for j in range(i + 1, len(wlist)):  # loop to compare each items in the list
            if wlist[j] < wlist[minIndex]: # if number is less than minimum
                minIndex = j #new minumum becomes that number
        if minIndex != i: #if minimum does not equal min, 
            swap(wlist,minIndex, i)  # Exchange item in the list
        i += 1 #move 1 space on to next number
        return wlist

def binarysearch(xnumlist, low, high, inputAnswer):   
        #looking for inputAnswer binary recursive
        mid = 0
        if low <= high:
            mid = (high + low) // 2
            #if element is present at middle
            if xnumlist[mid] == inputAnswer:
                return mid
            #if element is smaller than midpoint
            #look to the left
            elif xnumlist[mid] > inputAnswer:
                return binarysearch(xnumlist, low, mid - 1, inputAnswer)
            else:
                #if else element can only be present in right subarray
                return binarysearch(xnumlist, mid + 1, high, inputAnswer)
        else:
            print(low, high, inputAnswer, mid, len(xnumlist))
            #can not find elemet
            return -1
# Call the main function.
if __name__ == '__main__':
    main()
