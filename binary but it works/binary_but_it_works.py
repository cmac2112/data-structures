# Test Sorts and Searches
# programmer: Leroy Wilson
# Date: 9/1/2022

from os import execle
import time
import random
# This program generates random numbers. The numbers will be sorted
# and  particular number will be searched.

# main definition
def main():
    xnumlist = []  # List to hold random numbers
    xnum = 20000


    # Generate random numbers and add them to the a list
    for x in range(xnum):
        x = random.randint(1000000, 9999999)
        xnumlist.append(x)

    # sort the data
    selectionSort(xnumlist)

    # Get a random number in list to be search for test purposes
    numx =  random.randint(0, xnum)

    # enter an number to be searched.
    randnum = xnumlist[numx]
    print('test number:', numx)
    searchnum = int(input('Enter a number to search:'))
    start = int(round(time.time() * 1000))   # Start time

    # Determine if number is found
    index, found = search_num(xnumlist, randnum)
    end = int(round(time.time() * 1000)) # end  time

    # Print the formatted output
    printOutput(xnum, start, end, index, found)


# Search for the number to determine if found
def search_num(num, targAcct):
    chrgValid = False  # is it valid

    # Check if account is valid using sequential search
    # print("Number to be searched:" + str(targAcct))
    position = 0
    while position < (len(num)):
        if num[position] == targAcct:
            chrgValid = True
            return position, chrgValid
        position += 1

    # Return if charge Account is Valid or not.
    return -1, chrgValid


# Swap Function to exchange items in a list
def swap(wlist, i, j):
    # Exchange the items at positions i and j.
    temp = wlist[i]
    wlist[i] = wlist[j]
    wlist[j] = temp


# Print the formatted output
    # print the difference between start
    # and end time in milli. secs
    # Output String is defined by ‘<‘, ‘>’, ‘^’ and followed by the width number.
def printOutput(xnum, start, end, ix, found):
    print()

    # Determine difference
    tdiff = end - start
    # Print Report Headings
    print(f"{'# Search': <5}{'Start Time' : ^21}{'End Time' : ^15}{'Exec Time' : >21}")
    print(f"{xnum} \t {start} ms \t{end} ms \t{tdiff} ms")
    print()


# This function will sort the incoming list of numbers
# from the min to the max number.
def selectionSort(wlist):

    for i in range(len(wlist)): # loop though each item in the list
        minIndex = i
        for j in range(i + 1, len(wlist)):  # loop to compare each items in the list
            if wlist[j] < wlist[minIndex]:
                minIndex = j
        if minIndex != i:
            swap(wlist,minIndex, i)  # Exchange item in the list
        i += 1


# Call the main function.
if __name__ == '__main__':
    main()
