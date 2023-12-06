#semester project
#program to take an array of temperatures from years past and use such temperatures and trends to predict the next years temperatures
# Then use sort to find, warmest, coldest, coldest stretch, warmest stretch of the year

# Option to import your own temperatures
# Option to randomly generate temperatures accurate to what they may be in a specific location in real life
from os import lstat
from pdb import lasti2lineno
from tkinter import *
from tkinter import filedialog
import random
def list_creation(lst):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    counter = 0 #counter to determine what list is up
    if counter == 1:
        l1 = lst
        lst = [] #clear list
    if counter == 2:
        l2 = lst
        lst = []
    if counter == 3:
        l3 = lst
        lst = []
    if counter == 4:
        l4 = lst 
        lst = []
    if counter == 5:
        l5 = lst 
        lst = [] 
    else:
        counter += 1
    if len(l1) == 365: #checks if lists are full or not
        print("list 1 created...")
    else:
        l1 = lst
        randomizer(lst)
    if len(l2) == 365:
        print("list 2 created...")
    else:
        l2 = lst
        randomizer(lst)

    if len(l3) == 365:
        print("list 3 created...")
    else:
        l3 = lst
        randomizer(lst)

    if len(l4) == 365:
        print("list 4 created...")
    else:
        l4 = lst
        randomizer(lst)
    if len(l5) == 365:
        print("list 5 created...")
    else:
        l5 = lst
        randomizer(lst)

    printlist(l1, l2, l3, l4, l5)
def randomizer(lst):
        #for randomization boundaries will be highest and lowest avg temp for the month according to google, may add rudamentary fronts and boundaries if i have time
        #this may lead to sharp inclines of temperatures when months begin and end, 
        #adding fronts and boundaries would mitigate sharp spikes between months, but would also produce sharp spikes of their own like real world
        jan = 31
        feb = 28 #one month with 28
        mar = 31
        apr = 30
        may = 31
        jun = 30
        jul = 31
        aug = 31
        sep = 30
        octo = 31
        nov = 30
        dec = 31
        #avg temp in newton kansas jan = 
        for i in range(jan):
            lst.append(random.randint(20,40))
        for i in range(feb):
            lst.append(random.randint(24, 47))
        for i in range(mar):
            lst.append(random.randint(33, 56))
        for i in range(apr):
            lst.append(random.randint(42, 66))
        for i in range(may):
            lst.append(random.randint(54, 76))
        for i in range(jun):
            lst.append(random.randint(64, 86))
        for i in range(jul):
            lst.append(random.randint(69, 92))
        for i in range(aug):
            lst.append(random.randint(67, 91))
        for i in range(sep):
            lst.append(random.randint(58, 82))
        for i in range(octo):
            lst.append(random.randint(45, 69))
        for i in range(nov):
            lst.append(random.randint(33, 55))
        for i in range(dec):
            lst.append(random.randint(22, 42))
        list_creation(lst)
        #odd
        
        

def filech():

def main():
    lst = []
    print("Temperture Forecaster")
    print("--This program will take temperatures from years past and use them to predict the temperature for the next year--")
    sel = 0
    print("Enter 1 to randomize 5 past years of temperatures,")
    sel = int(input('Enter 2 to choose your files:'))
    if sel == 1:
        list_creation()
    elif sel == 2:
        filech()
def main()

def printlist(l1, l2, l3, l4, l5):
    print(l1)
    print('-----')
    print(l2)
    print('-----')
    print(l3)
    print('-----')
    print(l4)
    print('-----')
    print(l5)