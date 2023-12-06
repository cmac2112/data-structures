
# Number Analysis Program
# Enter a series of 20 numbers.
# The program; should store the numbers in a
# list then display the following data:
# lowest, highest, total and average.
# programmer: Leroy Wilson caden mcarthur
# date: 7/13/2021


#convert program from list to use arrays, customize program to personal specifications
import array as arr
# main definition
def main():
    # MSC Variables
    
    totalNumAnal = 0.0     # total NumAnal for the year
    avgNumbers = 0.0    # average monthly xnumfall
    hightestNum  = 0   # highest number
    lowestNum = 0        # lowest number
    logicalSize = 0 #logic size of array
    #physical size of array
    # Create an ARRAY to hold the monthly xnumfall
    numAnalysis = arr('f',[0] * 20) # 20 = pysical size of array
    print(numAnalysis)

    # enter the required numbers
    getNum(numAnalysis,logicalSize,DEFAULT_CAPACITY)

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
def getNum(a,logicalSize,Dcap): #increase index by 1 each pass
    #insert num at index + 1
    #return numAnalysis at 20 elements

    # Get a number
    index = 0
    print(a)
    print(logicalSize) #debug
    print(Dcap)
    print('arr, logic, dcap')


    num = int(input("Enter a number:"))
    if logicalSize <= 20:
        app_arr(logicalSize, a, Dcap, num)
        return index + 1
        
    else:
        print("array is full at 20")
        print(len(a))
        print('arr len') #debug
    return a #return to numAnalysis
def increase_size(logic, a, dcap):
    #increase size of array
    #then return back to app_arr

    if logic == len(a):
        temp = arr(len(a) + 1) #create new array
        for i in range(logic): #copy data from old array to new 
            temp [i] = a[i]     
        a = temp        #reset variable to new expanded array
        print(a)
        print('arr after one expansion')
    return a, logic, dcap

def app_arr(logic, a, dcap, num):
    a = a
    if logic == dcap:
        increase_size(logic, a, dcap, num)
        dcap += 1
        logic += 1
        return a
    else:
        a.insert(num)
        print(a)
    return logic, a, dcap

# Display the output
def displayOutput(totalNum, avgNum, highNum, lowNum, numAnalysis):
    print("=================================================")
    print()
    print("Numbers Entered:",(numAnalysis.itemsize))
    print("The total of the numbers in the array:\t", format(totalNum, '.2f'))
    print("The average number in the array     :\t", format(avgNum, '.2f'))
    print("The highest number in the array      :\t", highNum)
    print("The lowest number in the  array      :\t", lowNum)
    print()
    print("=================================================")

# Call the main function
main()
