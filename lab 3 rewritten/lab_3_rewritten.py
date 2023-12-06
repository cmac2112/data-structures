#caden mcarthur
#9/7/2022

import time
import random


def main():
    #variables
    inputamt = int(input('Enter the amount of elements you want to generate in the list:'))

    #user chooses the amount of elements present in the list
    #time varies between amounts of elements in list
    
    arr = []
    num = inputamt #number of numbers to generate
    genstart = time.time()
    
    for x in range(num):
        x = random.randint(1000000, 9999999) #generates the amount of random numbers inputed before
        arr.append(x) #appends the list to add them

    genend = time.time() #time check to see how long generation takes
    gentime = (genend - genstart)
    print('Generated:', inputamt, 'numbers in', round(gentime, 5), 'ms')
    print("sorting...")
    #sort list
    sortstart = time.time() #time check to see how long selection sorting takes
    selectionSort(arr)
    sortend = time.time()
    print("sorted ", inputamt, "numbers in: ", round((sortend - sortstart), 5), "seconds")
    numx = random.randint(0, num)
    print(f" Test number: {arr[numx]}")
    

    #get a number to be binary searched
    Ans = int(input('Enter a number to search: '))
    start = time.time() #begin search time
    result = binarySearch(arr, 0, len(arr)-1, Ans)


    #print results
    end = time.time()
    if (end - start) < 0.005: # if time is too small to round to 2 decimals, alert user
        print("time elapsed too small to round to 2 decimals, will round to 10 decimal places.")
        small = round((end-start), 10)
    else:
        print()
    
    if result == -1:
        print('Element not found in array')
        print('time elapsed:', round((end - start), 10), "ms") #rounding time to 2 decimal places
    else:
        print('Element found at index:',result)
        print('Total elements in array:', num)
        print('time elapsed:', round((end - start), 10), "ms") #rounding doesnt work sometimes just shows 0.0 doesnt make sense


def binarySearch(arr, low, high, Ans):
    #looking for ans in using binary recursive
    mid = 0
    if low <= high:
        mid = (high + low) // 2
        #if element is present at midpoint
        if arr[mid] == Ans:
            return mid #return the midpoint as found
        #if element is smaller, look to left
        elif arr[mid] > Ans:
            return binarySearch(arr, low, mid - 1, Ans) #recursive loop to look again only using left side
        else:
            #if not in left, then look right again
            return binarySearch(arr, mid + 1, high, Ans)
    else:
        #can not find element
        return -1

def swap(wlist, i, j):
    # Exchange the items at positions i and j.
    temp = wlist[i]
    wlist[i] = wlist[j]
    wlist[j] = temp
    
def selectionSort(wlist):

    for i in range(len(wlist)): # loop though each item in the list
        minIndex = i
        for j in range(i + 1, len(wlist)):  # loop to compare each items in the list
            if wlist[j] < wlist[minIndex]:
                minIndex = j
        if minIndex != i:
            swap(wlist,minIndex, i)  # Exchange item in the list
        i += 1
        #return messed things up
main()