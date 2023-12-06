# Number Analysis Program
# Enter a series of 20 numbers.
# The program; should store the numbers in a
# list then display the following data:
# lowest, highest, total and average.
# programmer: Leroy Wilson caden mcarthur
# date: 7/13/2021


#convert program from list to use arrays, customize program to personal specifications
import array as arr
import random
# main definition
def main():
    # MSC Variables
    NUMBERS = 20  # numbers to processed
    totalNumAnal = 0.0     # total NumAnal for the year
    avgNumbers = 0.0    # average monthly xnumfall
    hightestNum  = 0   # highest number
    lowestNum = 0        # lowest number

    #didnt want to type in 20 numbers every time see (getnum)
    arra = [5,9,5,9]

    print(arra)

    # Create an ARRAY to hold the monthly xnumfall #float
    array = arr.array('d',[0] * NUMBERS)
    

    # enter the required numbers
    getNum(array)

    # Get the total xnumfall for the year
    totalNumAnal = getTotalNumAnal(array)

    # Get the month with the highest xnumfall for the year
    hightestNum = getHighNumAnal(array)

    # Get the month with the lowest xnumfall for the year
    lowestNum = getLowNumAnal(array)

    # Get the average monthly xnumfall for the year
    avgNumbers = getAverage(array,totalNumAnal)
    print(array)

    # Display the output of the Num entries
    displayOutput(totalNumAnal, avgNumbers, hightestNum, lowestNum)


# get total xnumfall for the year
# @return  totalNum
def getTotalNumAnal(numAnalysis):
    totalNum = 0.0

    # Accumulate the sum of the elements
    # in the sales array.
    for i in range(len(numAnalysis)):
        totalNum += numAnalysis[i]

    # return the total
    return totalNum


# compute the average xnum
# @return avgNumaverage xnum
def getAverage(numAnalysis, total):
    avgNum = 0.0

    # Get the average xnumfall for the year
    avgNum = total /float(len(numAnalysis))

    # return average xnum
    return avgNum


# get the month with the highest xnumfall
# @return highNum
def getHighNumAnal(numAnalysis):
    highNum = numAnalysis[0]
    for i in range(len(numAnalysis)):
        if (numAnalysis[i] > highNum):
            highNum = numAnalysis[i]

    return highNum


# The getLowstMonth method determines the month
# with the lowest amount of xnumfall.
#   @return The number of the month with the lowest
#       amount of xnumfall.
def getLowNumAnal(numAnalysis):
    lowNum = numAnalysis[0]
    vmonth = " "
    for i in range(len(numAnalysis)):
        if (numAnalysis[i] < lowNum):
            lowNum = numAnalysis[i]

    return lowNum


# get a number from the user.
# @param entry list
def getNum(entry):
    # Get a number
    for i in range(len(entry)):
        # Prompt user for the number.
        tnum = i + 1
        array.append()
        
    return

# Display the output
def displayOutput(totalNum, avgNum, highNum, lowNum):
    print("=================================================")
    print()
    print("The total of the numbers in the list:\t", format(totalNum, '.2f'))
    print("The average number in the list      :\t", format(avgNum, '.2f'))
    print("The highest number in the list      :\t", highNum)
    print("The lowest number in the list       :\t", lowNum)
    print()
    print("=================================================")


# Call the main function
main()

