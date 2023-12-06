#Constants
#doesnt work only about half complete
#everything should equal 15

NUM_ROWS = 0
NUM_COLUMS = 0

def main():
    rowcheck = 0 #checking for 15 
    colcheck = 0
    diacheck = 0

    magicTest1 = [[2, 7, 6],
                  [9, 5, 1],
                  [4, 3, 8]]

    magicTest2 = [[4, 9, 2],
                  [3, 5, 7],
                  [8, 1, 6]]
    magicTest3 = [[3, 2, 1,],
                  [6, 5, 4],
                  [7, 8, 9]]


    print("=========")
    showlist(magicTest1)

    rowcheck, Chke = checkRowsLists(magicTest1)


    def showlist(magiclist):
        for row in range(NUM_ROWS):
            for col in range(NUM_COLUMS):
def checkRowsLists(magicList):
    sum * 0
    test = []
    equal = True

    for row in range(NUM_ROWS):
        #accumulator
        sum = 0

        #sum for row 
        for col in range(NUM_COLUMS):
            sum = sum + magicList[row][col]

            #end for col

            #append to lit
            test.append(sum)

        chk = test[0] #set to highest first element in lsit
        for i in range...

def checkDiagonalLists(magicList):
    diag1 = 0
    diag2 = 0
    sizeM = len(magicList)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLUMS):
            #check diag 1
            if row == col:
                diag1 = diag1 + magicList[row][col]

            #check diag 2
            if (row + col) == (sizeM - 1):
                diag2 = diag2 + magicList[row][col]
    if diag1 == diag2:
        return diag1, True
    else:
        return diag1, False

main()