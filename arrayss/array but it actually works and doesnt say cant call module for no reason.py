#num analysis
#caden mcarthur
#array


import array
def main():

    totalNumAnal = 0.0
    avgNumbers = 0.0
    hightestNum  = 0   # highest number
    lowestNum = 0        # lowest number
    logicalSize = 0

    #create base array to hold 20 elements
    numAnalysis = array.array('f',[0] * 20)
    print(numAnalysis)

     # enter the required numbers
    getNum(numAnalysis,logicalSize)

    # Get the total xnumfall for the year
    totalNumAnal = getTotalNumAnal(numAnalysis)

    # Get the month with the highest xnumfall for the year
    hightestNum = getHighNumAnal(numAnalysis)

    # Get the month with the lowest xnumfall for the year
    lowestNum = getLowNumAnal(numAnalysis)

    # Get the average monthly xnumfall for the year
    avgNumbers = getAverage(numAnalysis,totalNumAnal)
    print(numAnalysis)
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
def getNum(array, logic): #get number from user
    #insert number into the array at index + 1
    index = 0
    logic = 0
    loop = 0
    if loop > 1:
        index += 1
        logic += 1
        print(array)
        print("array")
    
        num = float(input("Enter number"))
    
        if logic == 20:
            return array
        else:
            array.insert(index, num)
            array.pop() #array acting as a list and expanding after every insert?
        
        return getNum(array, logic)
    return - 1
# Display the output
def displayOutput(totalNum, avgNum, highNum, lowNum):
    print("=================================================")
    print()
    print("The total of the numbers in the list:\t", format(totalNum, '.2f'))
    print("The average number in the list      :\t", format(avgNum, '.2f'))
    print("The highest number in the list      :\t", highNum)
    print("The lowest number in the list       :\t", lowNum)
    print("=================================================")


# Call the main function
main()

main()
