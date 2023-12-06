#caden mcarthur
#9/13/2022
#write program that reads names into list--
# use sort algorithm to sort in acending order--
#allow user to search for name in list--
#use binary search to perform--
#binary and sort are seperate functions--

def main():
    infile = open("names.txt", "r")
    #open and read file to list
    names = infile.read()

    nameslist = names.split("\n")
    infile.close()
    
    arr = sorting(nameslist)
    Ans = input("Enter Name to be searched, USE ALL CAPITAL LETTERS:")
    print(Ans)
    result = binarySearch(arr, 0, len(arr) - 1, Ans)

    if result == -1: #if search returns -1 it is not found
        print("Name not found in list")
    else:
        print("Name found at index:", result) #print where name is found if it is found at all
        #end

    

def sorting(nameList):
    l2 = []
 
    # create 2d list of names
    for ele in nameList:
        l2.append(ele.split())
    nameList = []
 
    # sort by name
    for ele in sorted(l2):
        nameList.append(' '.join(ele))
 
    # return sorted list
    print(nameList)
    return nameList

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
main()

